class Command:
    def execute(self):
        pass

class Ligths_On(Command):
    def execute(self):
        print("Light is on!")
        global last_command
        last_command = 1

class Lights_Off(Command):
    def execute(self):
        print("Light is off")
        global last_command
        last_command = 2

class Cancel_Last_Command:
    def execute(self):
        global last_command
        if last_command == 1:
            Lights_Off().execute()
        elif last_command == 2:
            Ligths_On().execute()


class RemoteControl:
    def __init__(self):
        self._commands = []

    def add_command (self, command):
        self._commands.append(command)

    def execute_commands(self):
        if self._commands:
            execute_command = self._commands.pop(0)
            execute_command.execute()

last_command = 0
remote = RemoteControl()
command = Ligths_On()
remote.add_command(command)
remote.execute_commands()

command = Cancel_Last_Command()
remote.add_command(command)
remote.execute_commands()