from commands import Command


class Help(Command):

    keywords = ["help", "h", "autsilio"]
    help_text = """lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Donec euismod, nisl eget consectetur sagittis, nisl nunc
    """

    def do_command(self, *args):
        if not args:
            self.show_help_text("help")
            return

        keyword = args[0]
        command = self.todo.commands.get(keyword)
        if not command:
            print(f"Unknown command: {keyword}")
            return
        command.show_help_text(keyword)

    def show_help_text(self, keyword):
        super().show_help_text(keyword)
