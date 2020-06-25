import os
from pathlib import Path

import click
from src.cmd.generate import execute

AWS_PROFILE_FILE = f"{str(Path.home())}/.aws/credentials"


@click.group()
def run():
    pass


@run.command(help="Generate a temporary token")
@click.option(
    "-p", "--profile", default=lambda: os.environ.get("AWS_PROFILE"), required=True, help="AWS profile to use",
)
@click.option("-u", "--user", required=True, help="AWS user name")
@click.option("-t", "--token", required=True, help="MFA Token")
def generate(profile, user, token):
    execute(AWS_PROFILE_FILE, profile, user, token)


@run.command(help="Create a configuration to manage your personnal access key")
@click.option("-e", "--expire", help="Number of day before the access key must be change")
@click.option("-p", "--profile", help="The local aws profile saved for your configuration")
@click.option("-u", "--user", help="The AWS user to manage access key")
def config():
    pass


@run.command(help="Rotate your personnal access key")
@click.option("-e", "--expire", help="Number of day before the access key must be change")
def rotate():
    pass
