def build_pipeline(schema):
    tasks = {
        "normalize": [],
        "sort_by_date": ["normalize"],
        "group_by_location": ["normalize"],
    }

    if "location" not in schema:
        tasks.pop("group_by_location")

    return tasks