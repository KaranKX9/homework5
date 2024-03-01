import pytest
from app import App
# tests/test_commands.py
from app.commands import CommandHandler, Command


def simulate_user_input(inputs):
    return lambda _: next(inputs)

def test_app_start_exit_command(capfd, monkeypatch):
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', simulate_user_input(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, _ = capfd.readouterr()
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', simulate_user_input(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_command_execution(capfd, monkeypatch, command, args, expected_output):
    inputs = iter([f'{command} {args}', 'exit'])
    monkeypatch.setattr('builtins.input', simulate_user_input(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, _ = capfd.readouterr()
    assert expected_output in out

def test_app_add_command(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'add', '1 2', '3')

def test_add_command_non_numeric_arguments(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'add', 'one two', 'Error: All arguments must be numeric')

def test_add_command_failure(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'add', '3', 'Require exact two arguments')

def test_app_subtract_command(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'sub', '5 2', '3')

def test_subtract_command_failure(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'sub', '10', 'Require exact two arguments')

def test_app_multiply_command(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'multi', '3 4', '12')

def test_multiply_command_failure(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'multi', '4', 'Require exact two arguments')

def test_app_divide_command(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'div', '8 2', '4')

def test_divide_command_div_by_zero(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'div', '20 0', "Can't division by zero")

def test_divide_command_failure(capfd, monkeypatch):
    test_command_execution(capfd, monkeypatch, 'div', '20', 'Require exact two arguments')
