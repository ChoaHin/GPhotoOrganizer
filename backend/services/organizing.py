#Logic for organizing files based on metadata.
import os
from backend.utils.file_ops import scan_dir, copy_files

def seperate_files(files):
    ''' Seperate files based on their type '''
    photos = []
    editedphotos = []
    videos = []
    metadata = []

    photo_ext = ['.png', '.jpg', '.webp']
    edited_ext = ['-edited.png', '-edited.jpg', '-edited.webp']
    video_ext = ['.mp4', '.mkv', '.avi']
    metadata_ext = ['.json', '.xml', '.csv']

    for file in files:
        file_str = str(file)
        if file_str.lower().endswith(tuple(edited_ext)):
            editedphotos.append(file)
        elif file_str.lower().endswith(tuple(photo_ext)):
            photos.append(file)
        elif file_str.lower().endswith(tuple(video_ext)):
            videos.append(file)
        elif file_str.lower().endswith(tuple(metadata_ext)):
            metadata.append(file)
    
    return photos, editedphotos, videos, metadata

def organize_files(source_folder, destination_folder):
    ''' Organize files based on their type '''
    # Define output directories
    photo_dir = destination_folder / 'photos'
    edited_dir = destination_folder / 'edited_photos'
    video_dir = destination_folder / 'videos'
    metadata_dir = destination_folder / 'metadata'

    # Create output directories if they don't exist
    photo_dir.mkdir(exist_ok=True)
    edited_dir.mkdir(exist_ok=True)
    video_dir.mkdir(exist_ok=True)
    metadata_dir.mkdir(exist_ok=True)

    # Scan source folder for files	
    files = scan_dir(source_folder)
    photos, editedphotos, videos, metadata = seperate_files(files)

    # Function to copy files to the appropriate directory
    copy_files(photos, photo_dir)
    copy_files(editedphotos, edited_dir)
    copy_files(videos, video_dir)
    copy_files(metadata, metadata_dir)

    print("Files organized successfully!")
    