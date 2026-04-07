# backend/main.py
import os
import sys
import json

# Add the backend directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import start here
from services.organizing import organize_files
from services.schema import infer_schema, normalize_data
from pathlib import Path
from utils.file_ops import load_all_json

def main():
    print("Image File Manager - Backend Running")
    sample_directory = Path("data/takeout-20240811T123851Z-001")
    output_directory = Path("data/output")

    # organize files
    organize_files(sample_directory, output_directory)

    # infer schema
    metadata_dir = output_directory / "metadata"
    data = load_all_json(metadata_dir)

    if not data:
        print("No metadata JSON records found.")
        return

    schema = infer_schema(data)
    
    # Output schema to file
    schema_file = output_directory / "schema.json"
    with open(schema_file, 'w') as f:
        json.dump(schema, f, indent=2)
    print(f"Schema written to {schema_file}")

    # normalized data
    normalized_data = normalize_data(data, schema)
    
    # Output normalized data to file
    normalized_file = output_directory / "normalized_data.json"
    with open(normalized_file, 'w') as f:
        json.dump(normalized_data, f, indent=2)
    print(f"Normalized data written to {normalized_file}")
if __name__ == "__main__":
    main()