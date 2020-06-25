import boto3
import sys
from ..internal import aws_config
from ..internal.token import token_valid, get_sesion_token


def execute(profile_path, profile, user_name, token):
    profile_config = aws_config.get(profile_path)

    if not profile_config.has_section(profile):
        sys.exit("The profile provided does not exists in your credential file\nPlease select a valid profile")

    session = boto3.session.Session(profile_name=profile)

    if not token_valid(token):
        print("The token must be composed by 6 digits")
        token = input("Token:\n")

    sts = session.client("sts")

    credentials = get_sesion_token(sts, user_name, token)

    aws_config.write(profile_path, profile, profile_config, credentials)
    print(f"Profile [{profile}-tmp] has been updated and will expire on {credentials['Credentials']['Expiration']}")
