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
        # clear()
        if args:
            if args[0] == 'pen' or args[0] == 'pending':
                self._pending()
                return
            # else:
            #     raise ValidationError(message=f"{args[0:]} not recogniced.")

        DATA = self.load_todo()
        contador = 0
        for item in DATA["tasks"]:
            contador += 1
            if item["state"] == 1:
                print(contador, "[•]", item["description"], "\n")
            else:
                print(contador, "[ ]", item["description"], "\n")

    def _pending(self, *args):
        DATA = self.load_todo()
        contador = 0
        for item in DATA["tasks"]:
            contador += 1
            if item["state"] == 0:
                print(contador, "[ ]", item["description"], "\n")
