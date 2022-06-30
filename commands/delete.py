from commands import Command

from prompt_toolkit.validation import Validator, ValidationError


class Delete(Command):

    keywords = ["delete", "del", "d"]
    help_text = """
                "delete", "del", "d"
                \tSummary: Delete a selected command.
                \tUsage: {keywords} <id>
    """

    def do_command(self, id=None):
        if id:
            _id = int(id) - 1
            if _id < 0:
                self.todo.rprompt_message = f"{self.todo.time_emoji} Task {id} invalid"
                return
            try:
                DATA = self.load_todo()
                del DATA["tasks"][_id]

            except IndexError:
                self.todo.rprompt_message = f"{self.todo.time_emoji} Task {id} invalid"
                return

            self.save_todo(DATA)
            list_open = self.todo.commands.get("list")
            list_open.do_command("list")

            # right prompt
            self.todo.rprompt_message = f"{self.todo.time_emoji} Task {id} deleted"
        else:
            self.todo.rprompt_message = f"{self.todo.time_emoji} No task selected"