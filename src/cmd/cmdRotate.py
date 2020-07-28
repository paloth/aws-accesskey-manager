import boto3
import sys

from ..internal import aws_config, keymgt


def execute(profile_path, deactivate, expire, profile, user_name, yes):
    print(f"Access Key rotation for profile {profile} ...")

    profile_config = aws_config.get(profile_path)

    if not profile_config.has_section(profile):
        sys.exit(f"The profile {profile} does not exists in your credential file\nPlease select a valid profile")

    if not profile_config.has_option(profile, "aws_access_key_id"):
        sys.exit(f"The profile {profile} does not have access key id configured")

    access_key_id = aws_config.get_profile_ak_id(profile, profile_config)

    session = boto3.session.Session(profile_name=profile)
    iam = session.client("iam")

    access_keys = iam.list_access_keys(UserName=user_name)

    access_key = keymgt.check_access_key_exist(access_key_id, access_keys)

    if keymgt.is_access_key_expired(access_key["CreateDate"], expire) is True:
        print("Your access key is expired ...")
        keymgt.renew(profile_config, iam, deactivate, profile, user_name)
