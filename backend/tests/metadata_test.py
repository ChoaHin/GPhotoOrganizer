#Tests for metadata extraction and handling.
import pytest
from backend.utils.metadata import parse_metadata

def test_parse_metadata(tmp_path):
    # Create a sample JSON file
    json_file = tmp_path / "sample.json"
    json_file.write_text('{"name": "sample_image.jpg", "date": "2021-01-01"}')
    
    # Parse the metadata
    metadata = parse_metadata(json_file)
    
    # Check if the metadata was parsed correctly
    assert metadata == {"name": "sample_image.jpg", "date": "2021-01-01"}
    