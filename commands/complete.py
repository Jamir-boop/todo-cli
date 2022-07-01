from commands import Command


class Complete(Command):
    keywords = ["complete", "done", "com", "f", "cc"]

    help_text = """
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
    
    """

    def do_command(self, *args):
        pass
