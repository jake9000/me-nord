#!/usr/bin/env python3
"""
compile_json.py — Read nord.css and write nord.json with the CSS content
JSON-escaped inside the "css" field.

Usage:
    python compile_json.py [--name "Nord"]

The script reads nord.css from the same directory as this script and writes
nord.json to the same directory. The output JSON is pretty-printed with
indentation for the top-level keys, but the "css" value is a compact
single-line string (no embedded literal newlines).
"""

import json
import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CSS_PATH = SCRIPT_DIR / "nord.css"
JSON_PATH = SCRIPT_DIR / "nord.json"
DEFAULT_NAME = "Nord"


def main() -> None:
    parser = argparse.ArgumentParser(description="Compile nord.css into nord.json")
    parser.add_argument(
        "--name",
        default=DEFAULT_NAME,
        help=f'Theme name (default: "{DEFAULT_NAME}")',
    )
    args = parser.parse_args()

    # Read the CSS source
    css_text = CSS_PATH.read_text(encoding="utf-8")

    # Build the output structure
    output = {
        "name": args.name,
        "css": css_text,
    }

    # Write JSON — json.dumps handles all escaping automatically.
    # The "css" value will contain literal \n sequences, which is exactly
    # what the Marinara Engine extension loader expects.
    JSON_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote {JSON_PATH}")


if __name__ == "__main__":
    main()