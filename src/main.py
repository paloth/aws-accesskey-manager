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


@run.command(help="Check access key age")
@click.option("--test", help="This is a test")
def check(test):
    pass


@run.command(help="Perform access key rotation")
def rotate():
    pass