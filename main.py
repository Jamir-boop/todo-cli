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



# historial persistente
session = PromptSession(history=FileHistory('.todo_history'))

while True:
    input = session.prompt('> ')
    if input.lower() == "list":


        # tasks = []

        # class task:
        #     def __init__(self, name, description, state):
        #         self.name = name
        #         self.description = description
        #         self.state = state

        


        for data in DATA["tasks"]:
            #name = data["id"]
            #description = data["description"]
            #state = data["state"]
            #tasks.append(task(name, description, state))

            print("Task:",data["id"],"\n",
                "\t", data["description"],"\n",
                "\t", data["state"],"\n")

    if input.lower() == "clear":
        clear()
        
      
    if input == "q" or input == "exit" or input == "quit":
        clear()
        break
