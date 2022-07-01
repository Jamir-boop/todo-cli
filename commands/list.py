# from prompt_toolkit.shortcuts import clear
from prompt_toolkit.validation import Validator, ValidationError

from commands import Command


class List(Command):
    keywords = ["list", "ls"]

    help_text = """
                
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
                List help text
    
    """

    def do_command(self, *args):
        self.order_completed_tasks()

        # clear()
        if args:
            if args[0] == 'pen' or args[0] == 'pending':
                self._pending()
                return

        DATA = self.load_todo()
        contador = 0
        for item in DATA["tasks"]:
            contador += 1
            if item["state"] == 1:
                self.print_style_text(
                    f"<number>{contador}</number> [•] <completed>{item['description']}</completed>\n")
            else:
                self.print_style_text(
                    f"<number>{contador}</number> [ ] <pending>{item['description']}</pending>\n")

        # right prompt
        self.todo.rprompt_message = f"{self.todo.time_emoji} All tasks!"

    def _pending(self, *args):
        DATA = self.load_todo()
        contador = 0
        for item in DATA["tasks"]:
            contador += 1
            if item["state"] == 0:
                self.print_style_text(
                    f"<number>{contador}</number> [ ] <pending>{item['description']}</pending>\n")
