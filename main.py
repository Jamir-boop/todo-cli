from ast import Delete, Return
from cgitb import text
import json
from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import clear

TODO = "todo.json"

###########################################
import json
from pydoc import describe

TODO = open('todo.json')
DATA = json.load(TODO)

clear()


def list(DATA):
    for data in DATA["tasks"]:
        print("Task:",data["id"],"\n",
            "\t", data["description"],"\n",
            "\t", data["state"],"\n")


def delete(DATA, data_id):
    for data in DATA["tasks"]:
        if data["id"] == data_id:
            DATA["tasks"].remove(data)



# historial persistente
session = PromptSession(history=FileHistory('.todo_history'))

while True:
    input = session.prompt('> ').lower().split()

    if input[0] == "list":
        list(DATA)

    if input[0] == "clear":
        clear()
    
    if input[0] == "del":
        try:
            delete(DATA, input[1])
            list(DATA)
        except:
            pass
              
    if input[0] == "q" or input[0] == "exit" or input[0] == "quit":
        clear()
        break
