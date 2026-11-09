from pathlib import Path

from xml_parser import parse_xml, print_fields


def main() -> None:
    data = Path("sample.xml").read_text(encoding="utf-8")
    required, optional = parse_xml(data)
    print_fields(required, optional)


if __name__ == "__main__":
    main()