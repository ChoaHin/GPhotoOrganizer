#Tests for file operation utilities.
import pytest
from backend.utils.file_ops import copy_file, move_file, organize_files

def test_copy_file(tmp_path):
    # Create a sample file
    src = tmp_path / "sample.txt"
    src.write_text("Sample file content")
    
    # Copy the file
    dest = tmp_path / "sample_copy.txt"
    copy_file(src, dest)
    
    # Check if the file was copied successfully
    assert dest.exists()
    assert dest.read_text() == "Sample file content"

def test_move_file(tmp_path):
    # Create a sample file
    src = tmp_path / "sample.txt"
    src.write_text("Sample file content")
    
    # Move the file
    dest = tmp_path / "sample_move.txt"
    move_file(src, dest)
    
    # Check if the file was moved successfully
    assert not src.exists()
    assert dest.exists()
    assert dest.read_text() == "Sample file content"