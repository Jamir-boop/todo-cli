from commands import Command


class Delete(Command):

    keywords = ["delete", "del", "d", "dd", "-"]
    help_text = """
                "delete", "del", "d"
                \tSummary: Delete a selected command.
                \tUsage: {keywords} <id>
    """

    def do_command(self, *args):
        if self.validate_task_selection(*args):
            self.print_style_text(
                f"<error>{self.validate_task_selection(*args)}</error>")
            return

        id = args[0]
        if id == "completed" or id == "com":
            self._delete_completed()
            return

        _id = int(id) - 1

        try:
            DATA = self.load_todo()
            del DATA["tasks"][_id]

        except IndexError:
            self.print_style_text(f"Task {id} invalid")
            return

        self.save_todo(DATA)
        list_open = self.todo.commands.get("list")
        list_open.do_command("list")

        self.print_style_text(f"<success>Task {id} deleted</success>")

    def _delete_completed(self):
        DATA = self.load_todo()
        contador = 0
        for item in DATA["tasks"]:
            if item["state"] == 1:
                del DATA["tasks"][contador]
            contador += 1

        self.save_todo(DATA)
        list_open = self.todo.commands.get("list")
        list_open.do_command("list")

        self.print_style_text(
            f"<success>All completed tasks deleted</success>")
