import sys
from app.commands import Command

class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2: self._handle_invalid_arguments(); return
        try: self._display_result(round(sum(map(float, args)), 1))
        except ValueError: self._handle_numeric_error()

    def _handle_invalid_arguments(self): print("Require exactly two arguments")
    def _handle_numeric_error(self): print("Error: All arguments must be numeric")
    def _display_result(self, result): print(result)
