import json

json1 = {"name": "Alice", "age": 30}
json2 = {"city": "New York", "country": "USA"}

merged_json = {**json1, **json2}  # Merge dictionaries
print(json.dumps(merged_json, indent=4))