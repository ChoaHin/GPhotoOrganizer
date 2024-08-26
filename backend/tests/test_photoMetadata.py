# tests/test_photo_metadata.py

from backend.classes.photoMetadata import photoMetadata

# Sample JSON data
json_data = {
    "title": "IMG_0957.JPG",
    "description": "",
    "imageViews": "50",
    "creationTime": {
        "timestamp": "1383737837",
        "formatted": "Nov 6, 2013, 11:37:17 AM UTC"
    },
    "photoTakenTime": {
        "timestamp": "1383179145",
        "formatted": "Oct 31, 2013, 12:25:45 AM UTC"
    },
    "geoData": {
        "latitude": 0.0,
        "longitude": 0.0,
        "altitude": 0.0,
        "latitudeSpan": 0.0,
        "longitudeSpan": 0.0
    },
    "geoDataExif": {
        "latitude": 0.0,
        "longitude": 0.0,
        "altitude": 0.0,
        "latitudeSpan": 0.0,
        "longitudeSpan": 0.0
    },
    "url": "https://photos.google.com/photo/AF1QipO6UevZ_6OGZGp792CQlFPaSMlZTZIEc7VOOvE"
}

def test_photo_metadata_parsing():
    # Create an instance from JSON data
    photo_metadata = photoMetadata.parse_json(json_data)

    # Perform assertions to check if data is parsed correctly
    assert photo_metadata.title == "IMG_0957.JPG"
    assert photo_metadata.description == ""
    assert photo_metadata.image_views == "50"
    assert photo_metadata.creation_time.strftime("%b %d, %Y, %I:%M:%S %p %Z") == "Nov 6, 2013, 11:37:17 AM UTC"
    assert photo_metadata.photo_taken_time['formatted'] == "Oct 31, 2013, 12:25:45 AM UTC"
    assert photo_metadata.geo_data['latitude'] == 0.0
    assert photo_metadata.geo_data['longitude'] == 0.0
    assert photo_metadata.geo_data_exif['latitude'] == 0.0
    assert photo_metadata.url == "https://photos.google.com/photo/AF1QipO6UevZ_6OGZGp792CQlFPaSMlZTZIEc7VOOvE"
