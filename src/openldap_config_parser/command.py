#!/usr/bin/env python3
from pathlib import Path

import click
from rich.console import Console
from rich.traceback import install

from openldap_config_parser import __name__, __version__
from openldap_config_parser.parser import parse

install(show_locals=True)


@click.command()
@click.version_option(version=__version__, package_name=__name__)
@click.help_option("-h", "--help")
@click.option("--dry-run", is_flag=True, help="dry run")
@click.argument("target", type=click.Path(exists=True))
def cli(target, dry_run):
    """
    \b
    TARGET      parse target file
    """
    console = Console()
    console.log("run script")
    parse(Path(target))
