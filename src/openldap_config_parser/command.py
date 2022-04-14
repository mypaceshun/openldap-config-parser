#!/usr/bin/env python3

import click
from rich.console import Console


@click.command()
def cli():
    console = Console()
    console.log("run script")
