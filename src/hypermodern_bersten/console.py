# src/hypermodern_bersten/console.py
import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.version_option(version=__version__)
@click.option("-l", "--language", default="en")
def main(language):
    """The Hypermodern Bersten Python project."""
    data = wikipedia.random_page(language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
