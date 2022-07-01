import datetime
from prompt_toolkit.shortcuts import clear

from commands import Command


class Create(Command):
    keywords = ['create', 'add', '+']

    help_text = """
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
    
    """

    def do_command(self, *args):
        if args:
            DATA = self.load_todo()
            last_id = int(DATA["tasks"][-1]["id"])  # toma ultimo del grupo
            last_id += 1
            DATA["tasks"].append(
                {
                    "id": last_id,
                    "priority": 2,
                    "description": args[1:],
                    "state": 0,
                    "time": f"{datetime.datetime.now()}"
                }
            )
            self.save_todo(DATA)
            self.todo.rprompt_message = f"{self.todo.time_emoji} Task {last_id} saved."
        else:
            self.todo.rprompt_message = f"{self.todo.time_emoji} Task has no content"
