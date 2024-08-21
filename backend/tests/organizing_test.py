import pytest
from pathlib import Path
from backend.services.organizing import seperate_files
from backend.utils.file_ops import scan_dir

def test_seperate_files():
    folder_path = Path('data/sample_photos')
    files = scan_dir(folder_path)
    photos, editedphotos, videos, metadata = seperate_files(files)

    assert len(photos) > 0
    assert len(editedphotos) > 0
    assert len(videos) == 0
    assert len(metadata) == 0

if __name__ == "__main__":
    pytest.main()
