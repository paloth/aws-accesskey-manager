from unittest.mock import patch
from akm.internal import keymgt
import pytest


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
