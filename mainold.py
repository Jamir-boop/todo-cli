import os
import importlib
import pkgutil
import sys
import json
from datetime import datetime
from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import clear
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML

BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__)))
TODO_FILE = f"{BASE_DIR}\\todo.json"


def reset_todo():
    DATA_INICIAL = {"tasks": [{"id": 12, "priority": 1, "description": "Primer pendiente y por eso el mejor", "time": "2022-06-04 20:29:28.294142", "state": 0}, {"id": 13, "priority": 0, "description": "crear clase de validator", "time": "2022-06-04 20:29:28.294142",
                                                                                                                                                                  "state": 0}, {"id": 22, "priority": 2, "description": "organizar clases", "time": "2022-06-04 20:29:28.294142", "state": 1}, {"id": 40, "priority": 2, "description": "este es un documento", "time": "2022-06-08 23:29:49.074971", "state": 0}]}
    with open(TODO_FILE, 'w') as file:
        file.seek(0)
        json.dump(DATA_INICIAL, file, indent=4)


def load_todo():
    with open(TODO_FILE) as file:
        return json.load(file)


def save_todo(data):
    with open(TODO_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def list():  # agregar buscador como argumento opcional
    clear()
    DATA = load_todo()
    contador = 0
    for item in DATA["tasks"]:
        contador += 1
        if item["state"] == 1:
            print(contador, "[•]", item["description"], "\n")
        else:
            print(contador, "[ ]", item["description"], "\n")


def create(input):
    description = ' '.join(input)

    DATA = load_todo()
    last_id = int(DATA["tasks"][-1]["id"])  # toma ultimo del grupo
    last_id += 1

    DATA["tasks"].append(
        {
            "id": last_id,
            "priority": 2,
            "description": description,
            "state": 0,
            "time": f"{datetime.now()}"
        }
    )
    save_todo(DATA)
    list()
    bottomToolbar.MESSAGE_GLOBAL = f"Task created"


def delete(id):
    id = int(id) - 1
    DATA = load_todo()

    try:
        del DATA["tasks"][id]

    except IndexError:
        raise ValidationError(message=f"{id+1} out of range.")

    save_todo(DATA)
    list()

    bottomToolbar.MESSAGE_GLOBAL = f"Task deleted"


def update(id, input):
    id = int(id) - 1
    description = ' '.join(input)

    DATA = load_todo()
    try:
        # atrapar error de fuera de indexs
        DATA["tasks"][id]["description"] = description
    except IndexError:
        raise ValidationError(message=f"{id+1} out of range.")
    save_todo(DATA)
    list()
    bottomToolbar.MESSAGE_GLOBAL = f"Task updated"


def complete(id):
    id = int(id) - 1
    DATA = load_todo()
    try:
        DATA["tasks"][id]["state"] = 1
    except IndexError:
        raise ValidationError(message=f"{id+1} out of range.")
    save_todo(DATA)
    list()


class InputValidator(Validator):
    def validate(self, document):
        text = document.text
        input = text.split()

        if len(input) != 0:
            # agregar opcion para listar solo pendientes
            if input[0] == "list" or input[0] == "ls":
                list()

            elif input[0] == "clear" or input[0] == "cls":
                clear()

            elif input[0] == "add" or input[0] == "create":
                create(input[1:])

            elif input[0] == "del":
                if len(input[1:]) == 1 and int(input[1]) >= 1:
                    delete(input[1])
                else:
                    raise ValidationError(
                        message='use "del <id>" to delete one task.')

            elif input[0] == "update" or input[0] == "up":
                if input[1].isnumeric() and int(input[1]) >= 1:
                    update(input[1], input[2:])
                else:
                    raise ValidationError(
                        message='use "up <id> <new task>" to update one task.')

            elif input[0] == "complete" or input[0] == "done":
                if input[1].isnumeric() and int(input[1]) >= 1:
                    complete(input[1])
                else:
                    raise ValidationError(
                        message='use "complete <id>" to mark task as completed.')

            elif input[0] == "q" or input[0] == "exit" or input[0] == "quit":
                exit()
            else:
                raise ValidationError(
                    message='Is not a todo-cli command (See "help")')


# mover estilo a style.py
style = Style.from_dict({
    # 'completion-menu.completion': 'bg:#008888 #ffffff',
    # 'completion-menu.completion.current': 'bg:#00aaaa #000000',
    # 'scrollbar.background': 'bg:#88aaaa',
    # 'scrollbar.button': 'bg:#222222',
    'rprompt': 'white bg:purple',
})


class bottomToolbar:
    MESSAGE_GLOBAL = '<style bg="black" fg="white">ctrl + d or ctrl + c to exit</style>'
# print(bottomToolbar.MESSAGE_GLOBAL)


def bottom_toolbar(text):
    output = text
    return HTML(output)


class rPrompt:
    MESSAGE_GLOBAL = ' Grupo actual: Tasks '


def get_rprompt(text):
    output = text
    return HTML(output)


commands = ['list', 'clear', 'del', 'add']
TODO_COMPLETER = WordCompleter(
    ['list', 'clear', 'del', 'add'], ignore_case=True)


class todoCompleter(Completer):
    def __init__(
        self,
        commands,
        ignore_case=False,
        meta_dict=None,
        WORD=False,
        sentence=False,
        match_middle=False
    ):
        assert not (WORD and sentence)
        self.commands = commands
        self.base_commands = sorted(list(commands.keys()))
        self.ignore_case = ignore_case
        self.meta_dict = meta_dict or {}
        self.WORD = WORD
        self.sentence = sentence
        self.match_middle = match_middle

    def get_completions(self, document, complete_event):
        # Get word/text before cursor.
        if self.sentence:
            word_before_cursor = document.text_before_cursor
        else:
            word_before_cursor = document.get_word_before_cursor(
                WORD=self.WORD)

        if self.ignore_case:
            word_before_cursor = word_before_cursor.lower()

        def word_matcher(word):
            """ True when the command before the cursor matches. """
            if self.ignore_case:
                word = word.lower()

            if self.match_middle:
                return word_before_cursor in word
            else:
                return word.startswith(word_before_cursor)

        suggestions = []
        document_text_list = document.text.split(" ")

        if len(document_text_list) < 2:
            suggestions = self.base_commands

        elif document_text_list[0] in self.base_commands:
            command = self.commands[document_text_list[0]]
            suggestions = command.get_suggestions(document_text_list) or []

        for word in suggestions:
            if word_matcher(word):
                display_meta = self.meta_dict.get(word, "")
                yield Completion(
                    word, -len(word_before_cursor), display_meta=display_meta
                )

# manita de gato


def load_commands(session, player_view):
    path = os.path.join(os.path.dirname(__file__), "commands")
    modules = pkgutil.iter_modules(path=[path])

    for loader, mod_name, ispkg in modules:
        # Ensure that module isn't already loaded
        if mod_name not in sys.modules:
            # Import module
            loaded_mod = import_module("commands." + mod_name)

            # Load class from imported module
            class_name = "".join([x.title() for x in mod_name.split("_")])
            loaded_class = getattr(loaded_mod, class_name, None)
            if not loaded_class:
                continue

            # Create an instance of the class
            instance = loaded_class(game, session, player_view)


def main_loop():
    reset_todo()

    bindings = KeyBindings()

    @bindings.add('c-c')
    def _(event):
        exit()

    list()
    session = PromptSession(history=FileHistory('.todo_history'))

    while True:
        # try:
        user_input = session.prompt(
            '$ ', validator=InputValidator(),
            validate_while_typing=False,
            completer=TODO_COMPLETER,
            style=style,
            key_bindings=bindings,
            rprompt=get_rprompt(rPrompt.MESSAGE_GLOBAL)
        )
        if not user_input:
            continue
        else:
            user_input = user_input.split()

        command = user_input[0] or None
        if not command:
            print("unknown command")
            continue

        command.do_command(*user_input[1:])

        # except (KeyboardInterrupt):
        #     pass
        # except Exception as e:
        #     traceback.print_exc()


if __name__ == "__main__":
    main_loop()
