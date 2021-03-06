from akm.internal import token

import pytest
from botocore.exceptions import ClientError
from unittest.mock import MagicMock


def test_token_validity():
    assert token.validity("12345") is False
    assert token.validity("1234567") is False
    assert token.validity("123456") is True
    assert token.validity("qwerty") is False


def test_get_session_token(sts_get_session_response, sts_get_caller_id_response):
    sts = MagicMock()
    sts.get_session_token.return_value = sts_get_session_response
    sts.get_caller_identity.return_value = sts_get_caller_id_response

    assert token.get_session_token(sts, "user", "000000") == sts_get_session_response


def test_get_caller_id_fails(sts_get_session_response, sts_get_caller_id_response, boto_standard_error):
    sts = MagicMock()
    sts.get_caller_identity = MagicMock(side_effect=ClientError(boto_standard_error, "Error"))

    with pytest.raises(ClientError) as error:
        token.get_session_token(sts, "user", "000000")
    assert "WhatEver" in str(error.value)


def test_get_session_token_fails(sts_get_session_response, sts_get_caller_id_response, boto_standard_error):
    sts = MagicMock()
    sts.get_session_token = MagicMock(side_effect=ClientError(boto_standard_error, "Error"))
    sts.get_caller_identity.return_value = sts_get_caller_id_response

    with pytest.raises(ClientError) as error:
        token.get_session_token(sts, "user", "000000")
    assert "WhatEver" in str(error.value)
