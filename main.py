import json
import utils
from datetime import datetime
from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import clear
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import print_formatted_text as print # reemplaza default print

TODO = "todo.json"

def bottom_toolbar():
    return HTML('This is a <b><style bg="ansired">Toolbar</style></b>!')


def list(): # necesita agregar opciones de formateo ("compact", "detailed")
    clear()
    file = open('todo.json', "r+")
    DATA = json.load(file)
    for item in DATA["tasks"]:
        if item["state"] == 1:
            print(item["id"], "√", item["description"], item["priority"], "\n")
        else:
            print(item["id"], "•", item["description"], "\n")

def delete(data_id):
    
    #print("#############################################")

    X =  json.load(open(TODO, "r+"))

    DATA = X

    X.close()

    print(DATA)

    #print(DATA)

    for data in DATA["tasks"]:
        if data["id"] == data_id:
            DATA["tasks"].remove(data)


    #print("#############################################")
    print(DATA["tasks"])



    
    
    


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

from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt
import argparse


class StringValidator(Validator):
    def validate(self, document):
        text = document.text
        
        if text and not text.isdigit():
            input = utils.parse(text)[0]

            if len(input) != 0:
                if input[0] == "list":
                    list()        
                if input[0] == "clear" or input[0] == "cls":
                    clear()
                if input[0] == "add":
                    create(input)
                    list()
                if input[0] == "del":
                    try:
                        delete(input[1])
                        list()
                    except:
                        pass

                if input[0] == "q" or input[0] == "exit" or input[0] == "quit":
                    exit()
        else:
            raise ValidationError(message='This input contains numeric characters')

###################### COMPLETER ################################

from prompt_toolkit.completion import WordCompleter

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