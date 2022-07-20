from commands import Command


class List(Command):
    keywords = ["list", "ls", "l"]

    help_text = """
                
                {keyword}
                {id}
                Summary: Get help for a command.
                Usage: {keyword} <command>
                List help text
    
    """

    def do_command(self, *args):
        self.sort_tasks()

        if args:
            if args[0] == 'pen' or args[0] == 'pending':
                self._pending()
                return

        DATA = self.load_todo()
        contador = 0
        for item in DATA["tasks"]:
            contador += 1
            if item["state"] == 1:
                self.print_style_text(
                    f"<number>{contador}</number> [•] <completed>{item['description']}</completed>\n")
            else:
                deadline = ""
                if item["deadline"] != "None":
                    deadline = self._time_left(item["deadline"])
                    deadline = f" • <deadline>{deadline} days left </deadline>"
                    
                if item["priority"] == 1:
                    self.print_style_text(
                        f"<number>{contador}</number> [ ] <high_priority>{item['description']}</high_priority>{deadline}\n")
                    continue
                else:
                    self.print_style_text(
                        f"<number>{contador}</number> [ ] <pending>{item['description']}</pending>{deadline}\n")

        # right prompt
        # pending = self._count_pending()
        # self.todo.rprompt_message = f"{pending} pending tasks! {self.todo.time_emoji}"
        self.todo.rprompt_message = f"{self.todo.time_emoji}"

    def _time_left(self, deadline):
        import datetime

        # calculate time left in days
        time_left = datetime.datetime.strptime(
            deadline, "%Y-%m-%d %H:%M:%S.%f") - datetime.datetime.now()
        return time_left.days

    def _pending(self):
        DATA = self.load_todo()
        contador = 0
        for item in DATA["tasks"]:
            contador += 1
            if item["state"] == 0:
                deadline = ""
                if item["deadline"] != "null":
                    deadline = self._time_left(item["deadline"])
                    deadline = f" • <deadline>{deadline} days left </deadline>"
                    
                if item["priority"] == 2:
                    self.print_style_text(
                        f"<number>{contador}</number> [ ] <high_priority>{item['description']}</high_priority>{deadline}\n")
                    continue
                else:
                    self.print_style_text(
                        f"<number>{contador}</number> [ ] <pending>{item['description']}</pending>{deadline}\n")

    def _count_pending(self):
        DATA = self.load_todo()
        pending = 0
        for item in DATA["tasks"]:
            if item["state"] == 0:
                pending += 1
        return pending
