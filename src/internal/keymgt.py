from datetime import datetime, timedelta

from dateutil.tz import tzutc
from . import aws_config
import sys

"""Access Key management"""


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


def renew(config, iam, deactivate, profile, user_name):
    new_ak = iam.create_access_key(UserName=user_name)

    current_ak = aws_config.get_profile_ak_id(profile, config)

    if deactivate:
        iam.update_access_key(
            UserName=user_name, AccessKeyId=current_ak, Status="Inactive",
        )
    else:
        iam.delete_access_key(UserName=user_name, AccessKeyId=current_ak)

    return new_ak
