from commands import Command

from prompt_toolkit.shortcuts import clear


class Update(Command):
    keywords = ["update", "up", "=", "edit"]

    help_text = """
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
    
    """

    def do_command(self, *args):
        if self.validate_task_selection(*args[0]):
            self.print_style_text(
                f"<error>{self.validate_task_selection(*args[0])}</error>")
            return

        DATA = self.load_todo()
        description = ' '.join(args[1:])
        _id = int(args[0]) - 1

        try:
            DATA["tasks"][_id]["description"] = description

        except IndexError:
            self.print_style_text(
                f"<error>{self.validate_task_selection(*args[0])}</error>")
            return

        self.save_todo(DATA)

        clear()
        list_open = self.todo.commands.get("list")
        list_open.do_command("list")

        self.print_style_text(f"<success>Task {args[0]} updated</success>")
