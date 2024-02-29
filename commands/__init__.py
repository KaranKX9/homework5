from abc import ABC, abstractmethod
from multiprocessing import Process

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        try:
            self._execute_valid_command(command_name, *args)
        except KeyError:
            self._handle_command_not_found(command_name)
        except Exception as e:
            self._handle_execution_error(command_name, e)

    def _execute_valid_command(self, command_name: str, *args):
        self.commands[command_name].execute(*args)

    def _handle_command_not_found(self, command_name: str):
        print(f"No such command: {command_name}")

    def _handle_execution_error(self, command_name: str, error: Exception):
        print(f"Error executing command '{command_name}': {error}")

# Example Usage:
class MyCommand(Command):
    def execute(self, arg1, arg2):
        print(f"Executing command with args: {arg1}, {arg2}")

handler = CommandHandler()
handler.register_command("my_command", MyCommand())

handler.execute_command("my_command", "arg1_value", "arg2_value")
handler.execute_command("unknown_command", "arg1_value", "arg2_value")
