import json
import utils
from datetime import datetime
from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import clear
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import print_formatted_text as print # reemplaza default print
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

TODO = "todo.json"
def reset_todo(): # para tests
    DATA_INICIAL = {"tasks":[{"id":12,"priority":1,"description":"Primer pendiente y por eso el mejor","time":"2022-06-04 20:29:28.294142","state":0},{"id":13,"priority":0,"description":"crear clase de validator","time":"2022-06-04 20:29:28.294142","state":0},{"id":22,"priority":2,"description":"organizar clases","time":"2022-06-04 20:29:28.294142","state":1},{"id":40,"priority":2,"description":"este es un documento","time":"2022-06-08 23:29:49.074971","state":0}]}
    with open(TODO, 'w') as file:
        file.seek(0)
        json.dump(DATA_INICIAL, file, indent=4)
reset_todo()

def list(): # necesita agregar opciones de formateo ("compact", "detailed")
    clear()
    file = open('todo.json', "r+")
    DATA = json.load(file)
    contador = 0
    for item in DATA["tasks"]:
        contador += 1
        if item["state"] == 1:
            print(contador, "√", item["description"], item["priority"], "\n")
        else:
            print(contador, "•", item["description"], "\n")

def load_todo():
    with open(TODO) as file:
        return json.load(file)

def save_todo(data):
    with open(TODO, 'w') as file:
        json.dump(data, file, indent=4)

def delete(id):
    DATA = load_todo()
    del DATA["tasks"][id-1]
    save_todo(DATA)


def create(input):
    with open(TODO, "r+") as file:
        description_index = input.index("add")

        last_index = len(input)
        description = ' '.join(input[description_index + 1:last_index])

        DATA = json.load(file)
        last_id = int(DATA["tasks"][-1]["id"])

        DATA["tasks"].append(
            {
                "id": str(last_id + 1),
                "description": description,
                "state": 0,
                "time": f"{datetime.now()}"
            }
        )

        file.seek(0)
        json.dump(DATA, file, indent=4)
        file.close()


# historial persistente
session = PromptSession(history=FileHistory('.todo_history'))


######################### VALIDATOR ##############################
class StringValidator(Validator):
    def validate(self, document):
        text = document.text
        
        if text and not text.isdigit():
            input = utils.parse(text)[0]

            if len(input) != 0:
                if input[0] == "list" or input[0] == "ls":
                    list()        
                if input[0] == "clear" or input[0] == "cls":
                    clear()
                if input[0] == "add":
                    create(input)
                    list()
                if input[0] == "del":
                    delete(int(input[1]))
                    list()

                if input[0] == "q" or input[0] == "exit" or input[0] == "quit":
                    exit()
        else:
            raise ValidationError(message='This input contains numeric characters')


CLI_COMPLETER = WordCompleter([
    'list','clear','del','add'], ignore_case=True)


######################### STYLE MENUS #########################
from prompt_toolkit.styles import Style

style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})



while True:
    input = session.prompt('> ', validator=StringValidator(),
                                 validate_while_typing=False,
                                 completer=CLI_COMPLETER,
                                 style=style)