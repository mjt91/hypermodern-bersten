# src/hypermodern_bersten/console.py
import textwrap

import click
import requests

from . import __version__

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
@click.option("-l", "--language", default="en")
def main(language):
    """The Hypermodern Bersten Python project."""
    global API_URL

    if language:
        API_URL = API_URL.replace("en", str(language), 1)

    with requests.get(API_URL) as response:
        try:
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
