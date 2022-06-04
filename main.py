import json
from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession

TODO = "todo.json"

# historial persistente
session = PromptSession(history=FileHistory('.todo_history'))

while True:
    text1 = session.prompt('> ')
    if text1.lower() == "list":
        with open(TODO, "r") as file:
            DATA = json.load(file)
            print(DATA)
    if text1 == "q" or text1 == "exit" or text1 == "quit":
        break
