import json

with open("sample.json", "r+") as file:
    input = {
        "id":"4",
        "email": "nikhil@geeksforgeeks.org",
        "job_profile": "Full Time"
    }
    
    DATA = json.load(file)
    DATA["tasks"].append(input)
    file.seek(0)
    json.dump(DATA, file,indent=4)
