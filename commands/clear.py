from prompt_toolkit.shortcuts import clear

from commands import Command


class Clear(Command):
    keywords = ['clear', 'cls', 'c']

    help_text = """
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
    
    """

    def do_command(self, *args):
        clear()