import json

from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.styles import Style

TODO_FILE = "todo.json"


class Command:
    keywords = []
    style = Style.from_dict(
        {
            # "completed": "#ffcc00 bold",
            # "pending": "#ffcc00",
            'high_priority': "peru bold",
            'completed': '#858585 italic',
            'pending': '#a8ff94',
            'number': '#a697e8 bold',
            'error': 'red bold',
            'success': 'green bold',
        }
    )

    def __init__(self, todo, session):
        self.reset_todo()
        self.todo = todo
        self.session = session

        for kw in self.keywords:
            todo.commands[kw] = self

        print("Registered " + self.__class__.__name__)

    def get_suggestions(self, words):
        return []

    def print_style_text(self, text):
        print_formatted_text(HTML(text), style=self.style)

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

    def reset_todo(self):
        DATA_INICIAL = {"tasks": [{"description": "Primer pendiente y por eso el mejor", "deadline": "2022-06-04 23:29:49.074971", "id": 12, "priority": 0, "state": 0}, {"description": "crear clase de validator", "deadline": "None", "id": 13, "priority": 0,
                                                                                                                                                                          "state": 0}, {"description": "organizar clases", "deadline": "None", "id": 22, "priority": 0, "state": 1}, {"description": "este es un documento con priority 1", "deadline": "2022-07-30 23:29:49.074971", "id": 40, "priority": 1, "state": 0}]}
        with open(TODO_FILE, 'w') as file:
            file.seek(0)
            json.dump(DATA_INICIAL, file, indent=4)

    def sort_tasks(self):
        data = self.load_todo()
        data["tasks"] = sorted(data["tasks"], key=lambda k: (
            k['state'], -k['priority'], k['deadline']))
        self.save_todo(data)

    def load_todo(self):
        with open(TODO_FILE) as file:
            return json.load(file)

    def save_todo(self, data):
        with open(TODO_FILE, 'w') as file:
            json.dump(data, file, indent=4)

    def validate_task_selection(self, *id):
        if not id:
            return "No task selected"

        if len(id) > 1:
            return "Select only one task"

        if not str(id[0]).isdigit():
            print(id)
            return "Invalid task id"

        return
