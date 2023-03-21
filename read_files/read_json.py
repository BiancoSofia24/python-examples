import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(ROOT_DIR, "file.json")
    
def load_json():
    with open(JSON_PATH) as file:
        return json.load(file)

data = load_json()
print("Json object:", data)

print("Data by key:", data["type"], data["name"])

credentials = data["credentials"]
print("Data by value:", credentials["username"], credentials["password"])

for client in data["clients"]:
    print("Clients:", client)