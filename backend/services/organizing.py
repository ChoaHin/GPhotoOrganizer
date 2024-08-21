#Logic for organizing files based on metadata.
import os
from backend.utils.file_ops import scan_dir

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