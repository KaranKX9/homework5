import pkgutil
import importlib
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        self._load_and_register_plugins_dynamically()

    def start(self):
        self.load_plugins()
        self._execute_initial_command()
        self._run_repl_loop()

    def _load_and_register_plugins_dynamically(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                self._register_commands_from_plugin(plugin_name, plugin_module)

    def _register_commands_from_plugin(self, plugin_name, plugin_module):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            try:
                if issubclass(item, Command):
                    self.command_handler.register_command(plugin_name, item())
            except TypeError:
                continue

    def _execute_initial_command(self):
        self.command_handler.execute_command('menu')

    def _run_repl_loop(self):
        while True:
            command_input = input(">>> ").strip()
            command_name, *args = command_input.split()
            self._execute_user_command(command_name, *args)

    def _execute_user_command(self, command_name, *args):
        self.command_handler.execute_command(command_name, *args)

