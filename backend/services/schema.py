def infer_schema(data):
    schema = {}

    for item in data:
        for key, value in item.items():
            if key not in schema:
                schema[key] = set()
            
            schema[key].add(type(value).__name__)

    return {key: sorted(list(types)) for key, types in schema.items()}

def normalize_data(data, schema):
    normalized = []

    for item in data:
        new_item = {}
        for key in schema:
            new_item[key] = item.get(key, None)
        normalized.append(new_item)
    return normalized