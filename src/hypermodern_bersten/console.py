# src/hypermodern_bersten/console.py
import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """The Hypermodern Bersten Python Project."""
    click.echo("Hello, world!")
