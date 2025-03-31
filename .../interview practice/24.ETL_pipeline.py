import json
import requests

def extract(url):
    response = requests.get(url)
    return response.json()

def transform(data):
    return [{ ("id" : item["id"], "name" : item["name"].upper())} for item in data]
            
def load(data,filename = "output.json"):
    with open(filename, "w") as f:
        json.dump(data, f)

url = "https://api.example.com/data"

raw_data = extract(url)
processed_data = transform(raw_data) 
load(processed_data)