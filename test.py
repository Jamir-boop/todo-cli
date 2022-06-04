from prompt_toolkit import PromptSession
from utils import import_file
data = import_file('todo.json')

# Create prompt object.
session = PromptSession()

# Do multiple input calls.
while True:
    text1 = session.prompt('> ')
    if text1.lower() == "list":
        print(data)
    if text1 == "q" or text1 == "exit" or text1 == "quit":
        break
