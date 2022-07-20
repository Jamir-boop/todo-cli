from commands import Command


class Sort(Command):
    keywords = ["sort"]

    help_text = """
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
    
    """

    def do_command(self, *args):
        data = self.load_todo()
        data["tasks"] = sorted(data["tasks"], key=lambda k: (
            k['state'], -k['priority'], k['deadline']))
        self.save_todo(data)
