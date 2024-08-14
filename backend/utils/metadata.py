#Functions to parse and extract metadata from the JSON files.
import json

def parse_metadata(json_file):
    ''' Parse metadata from a JSON file. '''
    try:
        with open(json_file, 'r') as file:
            metadata = json.load(file)
            return metadata
    except Exception as e:
        print(f"Error parsing metadata from {json_file}: {e}")
        return {}