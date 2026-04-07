def infer_schema(data):
    schema = {}

    for item in data:
        for key, value in item.items():
            if key not in schema:
                schema[key] = set()
            
            schema[key].add(type(value).__name__)

    return {key: sorted(list(types)) for key, types in schema.items()}

def normalize_data(data, schema):
    nomalized = []

    for item in data:
        new_item = {}
        for key in schema:
            if key in schema:
                new_item[key] = item.get[key, None]
            else:
                new_item[key] = None