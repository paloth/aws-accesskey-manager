from unittest.mock import patch, MagicMock
from akm.internal import keymgt
import pytest
from botocore.exceptions import ClientError


@patch("akm.internal.keymgt.datetime")
def test_is_delta_between_date_less_than_two_days(mock_datetime, current_mocked_date, creation_mocked_date):
    mock_datetime.now.return_value = current_mocked_date

    assert keymgt.is_access_key_expired(creation_mocked_date, 30) is True
    assert keymgt.is_access_key_expired(creation_mocked_date, 90) is False


def test_check_access_key_exist(iam_list_ak_response):

    assert keymgt.check_access_key_exist("AKIA111111111EXAMPLE", iam_list_ak_response) == {
        "AccessKeyId": "AKIA111111111EXAMPLE",
    }
    with pytest.raises(SystemExit) as sys_exit:
        keymgt.check_access_key_exist("AKIA111111111WRONG", iam_list_ak_response)
        assert sys_exit.type == SystemExit
        assert sys_exit.value.code == "Your profile access key does not match with an user access key"


def test_renew(iam_create_access_key_return):
    iam = MagicMock()
    aws_config = MagicMock()
    iam.create_access_key.return_value = iam_create_access_key_return
    iam.update_access_key.return_value = None

    aws_config.get_profile_ak_id.return_value = None
    deactivate = True

    assert keymgt.renew(aws_config, iam, deactivate, "profile", "user_name") == iam_create_access_key_return


def test_renew_fails(iam_limit_exceeded_exception):
    iam = MagicMock()
    iam.create_access_key = MagicMock(side_effect=ClientError(iam_limit_exceeded_exception, "create_access_key"))

    with pytest.raises(ClientError) as result:
        keymgt.renew("", iam, "", "", "")
        assert "LimitExceededException" in str(result.value)


def test_renew_deactivate_fails(iam_create_access_key_return, boto_standard_error):
    iam = MagicMock()
    aws_config = MagicMock()

    iam.create_access_key.return_value = iam_create_access_key_return
    iam.update_access_key = MagicMock(side_effect=ClientError(boto_standard_error, "create_access_key"))

    aws_config.get_profile_ak_id.return_value = None
    deactivate = True

    with pytest.raises(ClientError) as result:
        keymgt.renew(aws_config, iam, deactivate, "", "")
        assert "WhatEver" in str(result.value)


def test_renew_delete(iam_create_access_key_return):
    iam = MagicMock()
    aws_config = MagicMock()

    iam.create_access_key.return_value = iam_create_access_key_return
    iam.delete_access_key.return_value = None

    aws_config.get_profile_ak_id.return_value = None
    deactivate = False

    assert keymgt.renew(aws_config, iam, deactivate, "profile", "user_name") == iam_create_access_key_return


def test_renew_delete_fails(iam_create_access_key_return, boto_standard_error):
    iam = MagicMock()
    aws_config = MagicMock()

    iam.create_access_key.return_value = iam_create_access_key_return
    iam.delete_access_key = MagicMock(side_effect=ClientError(boto_standard_error, "create_access_key"))

    aws_config.get_profile_ak_id.return_value = None
    deactivate = False

    with pytest.raises(ClientError) as result:
        keymgt.renew(aws_config, iam, deactivate, "", "")
        assert "WhatEver" in str(result.value)
