import os
import sys
from pathlib import Path

import click

from src.cmd import cmdMfa, cmdRotate

AWS_PROFILE_FILE = f"{str(Path.home())}/.aws/credentials"


@click.group()
def run():
    pass


@run.command(help="Generate a temporary token with mfa")
@click.option(
    "-p",
    "--profile",
    default=os.environ.get("AWS_PROFILE", "default"),
    show_default=True,
    required=True,
    help="AWS profile to use. Take your current active profile or 'default' by default",
    type=str,
)
@click.option("-u", "--user", required=True, help="AWS user name", type=str)
@click.option("-t", "--token", required=True, help="MFA Token", type=str)
def mfa(profile, user, token):
    cmdMfa.execute(AWS_PROFILE_FILE, profile, user, token)


@run.command(help="Create a configuration to manage your personnal access key")
# @click.option("-e", "--expire", help="Number of day before the access key must be change")
# @click.option("-p", "--profile", help="The local aws profile saved for your configuration")
# @click.option("-u", "--user", help="The AWS user to manage access key")
def config():
    sys.exit("This feature will be implemented soon")


@run.command(help="Rotate your personnal access key")
@click.option("-e", "--expire", default=90, help="Number of day before the access key must be change", type=int)
@click.option(
    "-p",
    "--profile",
    default=os.environ.get("AWS_PROFILE", "default"),
    show_default=False,
    help="AWS profile to use. Take your current active profile or 'default' by default",
    type=str,
)
@click.option("-u", "--user", required=True, show_default=True, help="AWS user name to use", type=str)
@click.option(
    "-d",
    "--deactivate",
    is_flag=True,
    default=False,
    show_default=True,
    help="Deactivate the old Access Key instead of delete it",
    type=bool,
)
@click.option("-y", "--yes", is_flag=True, default=False, show_default=True, help="Validate action without prompt", type=bool)
def rotate(deactivate, expire, profile, user, yes):
    cmdRotate.execute(AWS_PROFILE_FILE, deactivate, expire, profile, user, yes)


if __name__ == "__main__":
    run()
