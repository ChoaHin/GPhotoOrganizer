# A model (or class) that defines the structure of the metadata parsed from JSON files.
from datetime import datetime


class photoMetadata:
    def __init__(self, title, description, image_views, creation_time, photo_taken_time, geo_data, geo_data_exif, url):
        self.title = title
        self.description = description
        self.image_views = image_views
        self.creation_time = self.convert_to_datetime(creation_time['timestamp'])
        self.creation_time_formatted = creation_time['formatted']
        self.photo_taken_time = self.convert_to_datetime(photo_taken_time['timestamp'])
        self.photo_taken_time_formatted = photo_taken_time['formatted']
        self.geo_data = geo_data
        self.geo_data_exif = geo_data_exif
        self.url = url

    def convert_to_datetime(self, timestamp):
        ''' Convert Unix timestamp to Python datetime object'''
        return datetime.utcfromtimestamp(int(timestamp))
    
    def __str__(self):
        return f"Title: {self.title}, Taken: {self.photo_taken_time_formatted}, Views: {self.image_views}"

    def get_location(self):
        ''' Get the location of the photo '''
        return (self.geo_data['latitude'], self.geo_data['longitude'])
    
    def to_dict(self):
        ''' Convert the object to a dictionary '''
        return {
            "title": self.title,
            "description": self.description,
            "image_views": self.image_views,
            "creation_time": self.creation_time_formatted,
            "photo_taken_time": self.photo_taken_time_formatted,
            "geo_data": self.geo_data,
            "geo_data_exif": self.geo_data_exif,
            "url": self.url
        }
    
    @classmethod
    def parse_json(cls, json_data):
        '''Create a PhotoMetadata object from a JSON string or dictionary'''
        if isinstance(json_data, dict):
            return cls(
            title=json_data['title'],
            description=json_data.get('description', ''),
            image_views=json_data.get('imageViews', '0'),
            creation_time=json_data['creationTime'],
            photo_taken_time=json_data['photoTakenTime'],
            geo_data=json_data['geoData'],
            geo_data_exif=json_data['geoDataExif'],
            url=json_data['url']
            )
        else:
            raise ValueError("Invalid JSON data provided")