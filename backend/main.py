import json
import os
from PIL import Image

def process_photo_data(json_path, image_folder):
    # Read JSON data
    with open(json_path) as f:
        data = json.load(f)
    
    # Extract information
    
    # photo_filename = data['photoFilename']
    # date_taken = data['photoTakenTime']['formatted']
    # location = data.get('geoData', {})
    photo_filename = data['url']
    date_taken = data['title']
    location = data['description']

    # Process the corresponding image
    image_path = os.path.join(image_folder, photo_filename)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        # Example: Print photo info
        print(f"Photo: {photo_filename}, Date: {date_taken}, Location: {location}")
        # Further processing like tagging, categorizing, etc.
    else:
        print(f"Image file for {photo_filename} not found.")

# Usage
process_photo_data('./jsons/example.json', './images/1.webp')
