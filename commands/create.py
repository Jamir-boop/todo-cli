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
        if not args:
            self.todo.rprompt_message = f"{self.todo.time_emoji} Task has no content"
            return

        DATA = self.load_todo()

        last_id = int(DATA["tasks"][-1]["id"])  # toma ultimo id del grupo
        last_id += 1

        description = ' '.join(args)
        DATA["tasks"].append(
            {
                "id": last_id,
                "priority": 2,
                "description": description,
                "state": 0,
                "time": f"{datetime.datetime.now()}"
            }
        )
        self.save_todo(DATA)

        list_open = self.todo.commands.get("list")
        list_open.do_command("list")

        self.todo.rprompt_message = f"{self.todo.time_emoji} Task {last_id} saved."
        
