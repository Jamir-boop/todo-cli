import os
import json

from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style

TODO_FILE = "todo.json"


class Command:
    keywords = []

    style = Style.from_dict(
        {
            "completion-menu.completion": "bg:#008888 #ffffff"
        }
    )

    def __init__(self, todo, session):
        self.todo = todo
        self.session = session

        for kw in self.keywords:
            todo.commands[kw] = self

        print("Registered " + self.__class__.__name__)

    def get_suggestions(self, words):
        return []

    def do_command(self, *args):
        print("nothing happens")

    def show_help_text(self, keyword):
        help_text = getattr(self, "help_text", None)
        if help_text:
            divider = "-" * len(keyword)
            # print(help_text.format(**locals()).strip())
            print(help_text.strip())
        else:
            print(f"No help text available for: {keyword}")

    def print(self, content):
        print_formatted_text(HTML(content), style=self.style)

    def reset_todo(self):
        DATA_INICIAL = {"tasks": [{"id": 12, "priority": 1, "description": "Primer pendiente y por eso el mejor", "time": "2022-06-04 20:29:28.294142", "state": 0}, {"id": 13, "priority": 0, "description": "crear clase de validator", "time": "2022-06-04 20:29:28.294142",
                                                                                                                                                                      "state": 0}, {"id": 22, "priority": 2, "description": "organizar clases", "time": "2022-06-04 20:29:28.294142", "state": 1}, {"id": 40, "priority": 2, "description": "este es un documento", "time": "2022-06-08 23:29:49.074971", "state": 0}]}
        with open(TODO_FILE, 'w') as file:
            file.seek(0)
            json.dump(DATA_INICIAL, file, indent=4)

    def load_todo(self):
        with open(TODO_FILE) as file:
            return json.load(file)

    def save_todo(self, data):
        with open(TODO_FILE, 'w') as file:
            json.dump(data, file, indent=4)
