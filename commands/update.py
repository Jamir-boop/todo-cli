from prompt_toolkit.shortcuts import clear

from commands import Command


class Update(Command):
    keywords = ['update', 'up', '=', 'edit']

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

        try:
            id = args[0]
            _id = int(id) - 1
        except ValueError:
            self.todo.rprompt_message = f"{self.todo.time_emoji} Task {id} invalid"
            return

        DATA = self.load_todo()
        description = ' '.join(args[1:])

        try:
            DATA["tasks"][_id]["description"] = description

        except IndexError:
            self.todo.rprompt_message = f"{self.todo.time_emoji} Task {id} invalid"
            return

        self.save_todo(DATA)

        list_open = self.todo.commands.get("list")
        list_open.do_command("list")

        self.todo.rprompt_message = f"{self.todo.time_emoji} Task {id} updated."
