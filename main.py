from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession

from utils import import_todo
DATA = import_todo()

# historial persistente
session = PromptSession(history=FileHistory('.todo_history'))

# Do multiple input calls.
while True:
    text1 = session.prompt('> ')
    if text1.lower() == "list":
        print(DATA)
    if text1 == "q" or text1 == "exit" or text1 == "quit":
        break
