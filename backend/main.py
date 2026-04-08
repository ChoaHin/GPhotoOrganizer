# backend/main.py
import os
import sys
import json

# Add the backend directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import start here
from backend.services import schema
from backend.services.executor import execute
from services.organizing import organize_files
from services.schema import infer_schema
from pathlib import Path
from utils.file_ops import load_all_json
from backend.services.functions import group_by_location, normalize_task, sort_by_date
from backend.services.pipeline import build_pipeline

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

    # Create execution context
    context = {
        "data": data,
        "schema": schema,
        "normalized": None
    }

    # Build pipeline
    tasks = build_pipeline(schema)

    # Register task functions
    functions = {
        "normalize": normalize_task,
        "sort_by_date": sort_by_date,
        "group_by_location": group_by_location
    }

    # Execute pipeline
    execute(tasks, functions, context)

    # Save output
    with open(output_directory / "normalized_data.json", 'w') as f:
        json.dump(context["normalized"], f, indent=2)

    print("Pipeline completed.")
    
if __name__ == "__main__":
    main()

    