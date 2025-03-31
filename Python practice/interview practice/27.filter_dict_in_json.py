import json

json_data = '''
[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
'''

data = json.loads(json_data)  # Convert JSON string to Python list
filtered_data = [person for person in data if person["age"] > 28]

print(json.dumps(filtered_data, indent=4))