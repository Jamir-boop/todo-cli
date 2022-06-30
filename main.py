import os
import sys
import pkgutil
import importlib

from importlib import import_module
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.history import FileHistory
from prompt_toolkit.validation import Validator, ValidationError

session = PromptSession(history=FileHistory('.todo_history'))


class Todo():
    base_dir = os.path.normpath(os.path.join(os.path.dirname(__file__)))
    commands = {}

    style = Style.from_dict(
        {
            'rprompt': 'white bg:purple',
        }
    )

    keybinds = KeyBindings()

    @keybinds.add('c-c')
    def _(event):
        exit()

    @keybinds.add('c-d')
    def _(event):
        exit()


class inputValidator(Validator):
    def __init__(self, todoobject):
        self.todoobject = todoobject

    def validate(self, document):
        text = document.text
        user_input = text.split()
        for i in user_input:
            if i == " ":
                return

        if user_input and not user_input[0] in self.todoobject.commands:
            raise ValidationError(message=f"Unknown command {text}")


def load_commands(todo, session):
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
            instance = loaded_class(todo, session)


def main_loop():
    todo = Todo()
    session = PromptSession()
    load_commands(Todo, session)

    def time_emoji():
        import datetime
        now = datetime.datetime.now()
        if now.hour >= 18 or now.hour < 6:
            print("🌙")
        else:
            print("🌞")

    # list when the app starts
    list_open = todo.commands.get("list")
    list_open.do_command("list")
    while True:
        user_input = session.prompt(
            "$ ",
            # completer=ClaseCOmpletadora(),
            # auto_suggest=AutoSuggestFromHistory(),
            validator=inputValidator(todo),
            key_bindings=todo.keybinds,
            style=todo.style,
        )
        if not user_input:
            continue
        else:
            user_input = user_input.split()

        command = todo.commands.get(user_input[0].lower()) or None
        if not command:
            print("Unknown command")
            continue

        command.do_command(*user_input[1:])


if __name__ == "__main__":
    main_loop()
