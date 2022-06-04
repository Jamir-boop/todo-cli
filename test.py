import json
TODO = "todo.json"

with open(TODO, "r+") as file:
    input = {
        "id":"4",
        "email": "nikhil@geeksforgeeks.org",
        "job_profile": "Full Time"
    }
    
    DATA = json.load(file)
    DATA["tasks"].append(input)
    file.seek(0) # seguimos sin saber que hace esta línea
    json.dump(DATA, file, indent=4)
