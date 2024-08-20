#Logic for organizing files based on metadata.
import os

def organize_files(path):
    # Get all the files in the given path.
    files = os.listdir(path)
    # Iterate through all the files.
    for file in files:
        # Get the full path of the file.
        file_path = os.path.join(path, file)
        # Check if the file is a directory.
        if file_path.is_dir():
            # Organize the files in the subdirectory.
            organize_files(file_path)
        else:
            