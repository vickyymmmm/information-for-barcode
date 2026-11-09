import xml.etree.ElementTree as ET

from field_definitions import REQUIRED_FIELDS


def parse_xml(data: str) -> tuple[dict[str, str], dict[str, str]]:
    """Parse XML and return (required_fields, optional_fields)."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise ValueError(f"Invalid XML: {exc}") from exc

    subfile = root.find("subfile[@designator='DL']")
    if subfile is None:
        raise ValueError("XML does not contain a DL subfile.")

    required = {}
    optional = {}

    for element in subfile.findall("element"):
        code = element.get("id")
        name = element.get("name") or code or "Unnamed field"
        value = "".join(element.itertext()).strip()

        if not code:
            continue

        if code in REQUIRED_FIELDS:
            required[REQUIRED_FIELDS[code]] = value
        else:
            optional[name] = value

    return required, optional


def print_fields(required: dict[str, str], optional: dict[str, str]) -> None:
    print("REQUIRED FIELDS")
    for name, value in required.items():
        print(f"  {name}: {value}")

    print("\nOPTIONAL FIELDS")
    for name, value in optional.items():
        print(f"  {name}: {value}")