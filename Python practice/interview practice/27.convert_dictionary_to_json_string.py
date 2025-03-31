import json

data = {"name" :" A", "age": 30}

json_string = json.dumps(data,indent=4)
print(json_string)