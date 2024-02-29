import pytest
from app import App
from unittest.mock import Mock

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    input_mock = Mock(side_effect=['exit'])
    monkeypatch.setattr('builtins.input', input_mock)
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
   
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
