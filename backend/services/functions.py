from backend.services import schema

def normalize_task(context):
    context["normalized"] = schema.normalize_data(context["data"], context["schema"])

def sort_by_date(context):
    context["normalized"].sort(key=lambda x: x["photoTakenTime"]["timestamp"] or "")

def group_by_location(context):
    groups = {}
    for item in context["normalized"]:
        loc = item["location"] or "Unknown"
        groups.setdefault(loc, []).append(item)
    print(groups)