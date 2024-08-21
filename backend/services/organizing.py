#Logic for organizing files based on metadata.
import os

def scan_files(files):
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
        if file.endswith(tuple(photo_ext)):
            photos.append(file)
        elif file.endswith(tuple(edited_ext)):
            editedphotos.append(file)
        elif file.endswith(tuple(video_ext)):
            videos.append(file)
        elif file.endswith(tuple(metadata_ext)):
            metadata.append(file)
    
    return photos, editedphotos, videos, metadata

