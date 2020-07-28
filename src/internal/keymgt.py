from datetime import datetime, timedelta

import boto3
from botocore.exceptions import ClientError
from dateutil.tz import tzutc
from . import aws_config
import sys

"""Access Key management"""


def convert_to_date(date_to_convert):
    """Convert the date format """
    try:
        return datetime.strptime(date_to_convert, "%Y-%m-%dT%H:%M:%S")
    except ValueError as error:
        raise error


def is_access_key_expired(date, days):
    """
    Check if the delta between the current date and the data date is greater than 90 days
    datetime.datetime(2020, 3, 20, 22, 6, 14, tzinfo=tzutc())}]
    """
    if (datetime.now().replace(tzinfo=tzutc(), microsecond=0) - date.replace(microsecond=0)) >= timedelta(days=days):
        return True
    else:
        return False


def check_access_key_exist(profile_ak, user_ak):
    flag = False
    while flag is False:

        for ak in user_ak["AccessKeyMetadata"]:
            if ak["AccessKeyId"] == profile_ak:
                flag = True
                return ak

        if flag is False:
            sys.exit("Your profile access key does not match with an user access key")


# def renew(config, iam, deactivate, profile, user_name):
#     new_key = iam.create_access_key(UserName=user_name)
#     current_ak = aws_config.get_profile_ak_id(profile, config)
#     if deactivate:
#         iam.update_access_key(
#             UserName=user_name, AccessKeyId=key["AccessKeyId"], Status="Inactive",
#         )


def check(config, user_name, profile, path):
    session = boto3.session.Session(profile_name=f"{profile}-tmp")
    iam = session.client("iam")
    try:
        current_keys = iam.list_access_keys(UserName=user_name)
    except ClientError as error:
        raise error

    for key in current_keys["AccessKeyMetadata"]:
        if is_access_key_expired(key["CreateDate"]):
            new_key = iam.create_access_key(UserName=user_name)
            if aws_config.update_profile(path, profile, config, new_key):
                try:
                    iam.update_access_key(
                        UserName=user_name, AccessKeyId=key["AccessKeyId"], Status="Inactive",
                    )
                except ClientError as error:
                    raise error

                print("Your access key is expired and has been updated")
            else:
                return False
        else:
            remaining_days = (key["CreateDate"] + timedelta(days=90)) - datetime.now().replace(tzinfo=tzutc())
            print(f"Your access key will expire in {remaining_days.days} days ")

    return True
