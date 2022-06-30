from commands import Command


class Delete(Command):

    keywords = ["delete", "del", "d"]
    help_text = """
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
    
    """

    def do_command(self, *args):
        print("delete deletiando")
