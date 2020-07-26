import os
from pathlib import Path

import click


from .cmd import cmdRotate, cmdMfa
import sys


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
    help="AWS profile to use",
)
@click.option("-u", "--user", required=True, help="AWS user name")
@click.option("-t", "--token", required=True, help="MFA Token")
def mfa(profile, user, token):
    cmdMfa.execute(AWS_PROFILE_FILE, profile, user, token)


@run.command(help="Create a configuration to manage your personnal access key")
# @click.option("-e", "--expire", help="Number of day before the access key must be change")
# @click.option("-p", "--profile", help="The local aws profile saved for your configuration")
# @click.option("-u", "--user", help="The AWS user to manage access key")
def config():
    sys.exit("This feature will be implemented soon")


@run.command(help="Rotate your personnal access key")
@click.option("-e", "--expire", default=90, help="Number of day before the access key must be change")
@click.option(
    "-p", "--profile", default=os.environ.get("AWS_PROFILE", "d2si"), show_default=True, help="AWS profile to use",
)
@click.option(
    "-u", "--user", required=True, show_default=True, help="AWS user name to use",
)
@click.option(
    "-d", "--deactivate", default=False, show_default=True, help="Deactivate the old Access Key instead of delete it",
)
@click.option(
    "-y", "--yes", default=False, show_default=True, help="Validate action without prompt",
)
def rotate(deactivate, expire, profile, user, yes):
    cmdRotate.execute(AWS_PROFILE_FILE, deactivate, expire, profile, user, yes)
