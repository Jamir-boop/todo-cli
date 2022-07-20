import datetime
from distutils.command.clean import clean
from tabnanny import check

from prompt_toolkit.shortcuts import clear

from commands import Command


class Create(Command):
    keywords = ["create", "add", "+", "new"]

    help_text = """
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
    
    """

    def do_command(self, *args):
        if not args:
            self.print_style_text(f"Task has no content")
            return

        DATA = self.load_todo()

        last_id = int(DATA["tasks"][-1]["id"])  # toma ultimo id del grupo
        last_id += 1

        deadline_check_list = ["days:", "d:"]
        priority_check_list = ["priority", "++"]
        check_list = deadline_check_list + priority_check_list
        deadline = self._check_days(args, deadline_check_list)
        priority = self._check_priority(args, priority_check_list)

        clean_args = self._clean_args(check_list, args)

        description = ' '.join(clean_args)
        DATA["tasks"].append(
            {
                "id": last_id,
                "priority": priority,
                "description": description,
                "state": 0,
                "deadline": f"{deadline}"
            }
        )

        self.save_todo(DATA)

        clear()
        list_open = self.todo.commands.get("list")
        list_open.do_command("list")
        self.print_style_text(f"<success>New task saved.</success>")

    def _clean_args(self, check_list, args):
        clean_list = []
        salida = []

        for word in args:
            for item in check_list:
                if word.startswith(item):
                    clean_list.append(word)

        for word in args:
            if not word in clean_list:
                salida.append(word)
        return salida

    def _check_days(self, args, check_list):
        for word in args:
            for item in check_list:
                if word.startswith(item):
                    days = "".join(filter(str.isdigit, word))
                    days = int(days)
                    return datetime.datetime.now() + datetime.timedelta(days=days)
        return None

    def _check_priority(self, args, check_list):
        for word in check_list:
            if word in args:
                return 1
        return 0
