# backend/main.py
import os
import sys
import json

# Add the backend directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import start here
from services.organizing import organize_files
from services.schema import infer_schema
from pathlib import Path


def load_metadata_json_records(metadata_dir: Path):
    """Load all JSON payloads from metadata_dir into a single list of records."""
    records = []

    for json_file in metadata_dir.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            payload = json.load(f)

        if isinstance(payload, list):
            records.extend(payload)
        elif isinstance(payload, dict):
            records.append(payload)

    return records

def main():
    print("Image File Manager - Backend Running")
    sample_directory = Path("data/takeout-20240811T123851Z-001")
    output_directory = Path("data/output")

    # organize files
    organize_files(sample_directory, output_directory)

    # infer schema
    metadata_dir = output_directory / "metadata"
    data = load_metadata_json_records(metadata_dir)

    if not data:
        print("No metadata JSON records found.")
        return

    schema = infer_schema(data)
    print("Inferred Schema:", schema)
if __name__ == "__main__":
    main()