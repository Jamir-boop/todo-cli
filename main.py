from ast import Delete, Return
from cgitb import text
import json
from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import clear
from prompt_toolkit.formatted_text import HTML


TODO = "todo.json"

###########################################
import json
from pydoc import describe

TODO = open('todo.json')
DATA = json.load(TODO)

clear()


def bottom_toolbar():
    return HTML('This is a <b><style bg="ansired">Toolbar</style></b>!')


def list(DATA):
    for data in DATA["tasks"]:
        print("Task:",data["id"],"\n",
            "\t", data["description"],"\n",
            "\t", data["state"],"\n")


def delete(DATA, data_id):
    for data in DATA["tasks"]:
        if data["id"] == data_id:
            DATA["tasks"].remove(data)


def create(DATA, input):
    description_index = input.index("-d")
    last_index = len(input)
    description = ' '.join(input[description_index+1:last_index])

    last_id = int(DATA["tasks"][-1]["id"])
    
    DATA["tasks"].append(
        {
            "id": str(last_id + 1),
            "description": description,
            "state": "incomplete"
        }
    )


# historial persistente
session = PromptSession(history=FileHistory('.todo_history'))

try:

    while True:
        
        input = session.prompt('> ', bottom_toolbar=bottom_toolbar).lower().split()
        
        if len(input) != 0:
                
            #Create
            if input[0] == "create":
                clear()
                try:    
                    create(DATA, input) 
                    list(DATA)            
                except:
                    print("A task need a description")
                    pass

            #Read
            if input[0] == "list":
                clear()
                list(DATA)

            
            if input[0] == "clear":
                clear()
            
            #Delete
            if input[0] == "del":
                clear()
                try:
                    delete(DATA, input[1])
                    list(DATA)
                except:
                    pass
                    
            if input[0] == "q" or input[0] == "exit" or input[0] == "quit":
                clear()
                break

except KeyboardInterrupt:
    clear()
    exit()