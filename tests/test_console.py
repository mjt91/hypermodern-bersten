# tests/test_console.py
import click.testing

from hypermodern_bersten import console


def test_main_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
