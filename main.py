from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession

TODO = "todo.json"

###########################################
import json
from pydoc import describe

TODO = open('todo.json')
DATA = json.load(TODO)



# historial persistente
session = PromptSession(history=FileHistory('.todo_history'))

# Do multiple input calls.
while True:
    text1 = session.prompt('> ')
    if text1.lower() == "list":


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
      
    if text1 == "q" or text1 == "exit" or text1 == "quit":
        break
