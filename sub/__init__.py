import sys
from app.commands import Command

class SubCommand(Command):
    def execute(self, *args): print(round(float(args[0]) - float(args[1]), 1)) if len(args) == 2 else print("Require exactly two arguments")
