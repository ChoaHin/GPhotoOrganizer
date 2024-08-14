# backend/main.py
import os
import sys

# Add the backend directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.utils.file_ops import organize_files
from backend.utils.metadata import parse_metadata

def main():
    print("Image File Manager - Backend Running")
    sample_directory = "data/sample_photos"
    sample_json = "data/sample_jsons/sample.json"

    # Parse metadata (example)
    metadata = parse_metadata(sample_json)
    print("Parsed Metadata:", metadata)

    # Organize files (example)
    organize_files(sample_directory, metadata)

if __name__ == "__main__":
    main()