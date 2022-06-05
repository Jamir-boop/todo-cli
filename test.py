import json
TODO = "todo.json"

with open(TODO, "r+") as file:
    input = {
        "id":"4",
        "description": "nikhil@geeksforgeeks.org",
        "state": "incomplete"
    }
    
    DATA = json.load(file)
    DATA["tasks"].append(input)
    file.seek(0)
    json.dump(DATA, file, indent=4)