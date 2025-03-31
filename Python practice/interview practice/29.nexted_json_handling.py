import json

# Sample nested JSON
nested_json = {
    "user": {
        "name": "Alice",
        "age": 25,
        "address": {
            "city": "NYC",
            "zip": "10001"
        }
    }
}

# Access nested values
city = nested_json["user"]["address"]["city"]

# Flatten JSON (convert nested keys to dot notation)
def flatten_json(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flat_json = flatten_json(nested_json)
print(flat_json)  # {'user.name': 'Alice', 'user.age': 25, 'user.address.city': 'NYC', 'user.address.zip': '10001'}

# Convert JSON to string and back
json_str = json.dumps(nested_json, indent=2)
parsed_json = json.loads(json_str)