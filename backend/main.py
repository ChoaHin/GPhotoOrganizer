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
    sample_directory = Path("data/sample_photos")
    sample_json = "data/sample_jsons/sample.json"

    # Organize files (example)
    organize_files(sample_directory)

if __name__ == "__main__":
    main()