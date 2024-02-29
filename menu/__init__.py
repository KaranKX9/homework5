import sys
from app.commands import Command

class MenuCommand(Command):
    def execute(self): print("\n\n:: Plugins Instructions ::\nPlugin Menu - menu\nAddition - add <number> <number>\nSubtraction - sub <number> <number>\nMultiplication - multi <number> <number>\nDivision - div <number> <number>\nExit - exit\n\n")
