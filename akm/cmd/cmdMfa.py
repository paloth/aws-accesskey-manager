import sys

import boto3

from akm.internal import aws_config, token


def execute(profile_path, profile, user_name, user_token):
    profile_config = aws_config.get(profile_path)

    if not profile_config.has_section(profile):
        sys.exit(f"The profile {profile} does not exists in your credential file\nPlease select a valid profile")

    while not token.validity(user_token):
        print("The token must be composed by 6 digits")
        user_token = input("Token:\n")

    session = boto3.session.Session(profile_name=profile)

    sts = session.client("sts")

    credentials = token.get_session_token(sts, user_name, user_token)

    aws_config.write(profile_path, profile, profile_config, credentials)
    print(f"Profile [{profile}-tmp] has been updated and will expire on {credentials['Credentials']['Expiration']}")
