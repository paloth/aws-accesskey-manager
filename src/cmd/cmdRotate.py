import boto3
import sys

from ..internal import aws_config


def execute(profile_path, deactivate, expire, profile, user_name, yes):
    print(f"Access Key rotation for profile {profile} ...")

    profile_config = aws_config.get(profile_path)

    if not profile_config.has_section(profile):
        sys.exit(f"The profile {profile} does not exists in your credential file\nPlease select a valid profile")

    if not profile_config.has_option(profile, "aws_access_key_id"):
        sys.exit(f"The profile {profile} does not have access key id configured")

    access_key_id = aws_config.get_profile_ak_id(profile, profile_config)
    # TODO Get AccessKey information
    session = boto3.session.Session(profile_name=profile)
    iam = session.client("iam")

    access_keys = iam.list_access_keys(UserName=user_name)
    # TODO Check user AK ID with profile AK ID

    for ak in access_keys["AccessKeyMetadata"]:
        if ak["AccessKeyId"] == access_key_id:
            pass
        else:
            sys.exit("Your profile access key id doesn't match with the user access key id")
