import sys
from app.commands import Command

class DivCommand(Command):
    def execute(self, *args):
        if len(args) != 2: self._handle_invalid_arguments(); return
        divisor = float(args[1])
        if divisor == 0: self._handle_division_by_zero(); return
        self._display_result(round(float(args[0]) / divisor, 1))

    def _handle_invalid_arguments(self): print("Require exactly two arguments")
    def _handle_division_by_zero(self): print("Can't divide by zero")
    def _display_result(self, result): print(result)

