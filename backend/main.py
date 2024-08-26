# backend/main.py
import os
import sys

# Add the backend directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import start here
from services.organizing import organize_files
from pathlib import Path

def main():
    print("Image File Manager - Backend Running")
    sample_directory = Path("data/takeout-20240811T123851Z-001")
    sample_json = "data/sample_jsons/sample.json"

    # Organize files (example)
    organize_files(sample_directory, Path("data/output"))

if __name__ == "__main__":
    main()