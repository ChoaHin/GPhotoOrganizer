#Functions for file operations like copying, moving, renaming files, and managing directories.
import os
import shutil

def copy_file(src, dest):
    ''' Copy a file from src to dest '''
    try:
        shutil.copy(src, dest)
        print(f"File copied from {src} to {dest}")
    except Exception as e:
        print(f"Error copying file from {src} to {dest}: {e}")

def move_file(src, dest):
    ''' Move a file from src to dest'''
    try:
        shutil.move(src, dest)
        print(f"File moved from {src} to {dest}")
    except Exception as e:
        print(f"Error moving file from {src} to {dest}: {e}")

def scan_dir(path):
    ''' Recursively scan the selected folder for all files '''
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if file_path.is_dir():
            scan_dir(file_path)
    return files