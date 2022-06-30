from prompt_toolkit.shortcuts import clear

from commands import Command


class Exit(Command):

    keywords = ["q", "quit", "exit"]
    help_text = """
                exit text help
    """

    def get_suggestions(self, words):
        return list(sorted(self.todo.commands.keys()))

    def do_command(self, *args):
        clear()
        exit()
