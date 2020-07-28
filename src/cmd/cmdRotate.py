import boto3

# from botocore.exceptions import ClientError
import sys

from ..internal import aws_config, keymgt
from datetime import datetime, timedelta
from dateutil.tz import tzutc


def change_key(profile_config, profile_path, iam, deactivate, profile, user_name):
    key = keymgt.renew(profile_config, iam, deactivate, profile, user_name)
    aws_config.update_profile(profile_path, profile, profile_config, key)
    print("Your access key has been renewed")


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
        change_key(profile_config, profile_path, iam, deactivate, profile, user_name)

    else:
        if yes:
            change_key(profile_config, profile_path, iam, deactivate, profile, user_name)

        else:
            print("Your access key is not expired ...")
            answer = input("Do you want to change it anyway ? (Only 'yes' is good answer)")

            if answer.lower == "yes":
                change_key(profile_config, profile_path, iam, deactivate, profile, user_name)

            else:
                remaining_days = (access_key["CreateDate"] + timedelta(days=expire)) - datetime.now().replace(tzinfo=tzutc())
                print(f"Your access key will expire in {remaining_days.days} days ")
                sys.exit("The key has not been renewed")
