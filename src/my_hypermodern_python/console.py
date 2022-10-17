import textwrap

import click

from . import __version__, wikipedia

from src.my_hypermodern_python.wikipedia import Page


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """The hypermodern Python project."""
    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))
