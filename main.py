import json
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

while True:
    text1 = session.prompt('> ')
    if text1.lower() == "list":
<<<<<<< HEAD


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
      
=======
        with open(TODO, "r") as file:
            DATA = json.load(file)
            print(DATA)
>>>>>>> cabe1670b5c91a15de69b659402eaeca9cea3d85
    if text1 == "q" or text1 == "exit" or text1 == "quit":
        break
