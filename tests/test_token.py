from src.internal.token import validity, get_sesion_token

import pytest
from botocore.exceptions import ClientError
from unittest.mock import MagicMock


def test_token_validity():
    assert validity("000000") is True
    assert validity("12345") is False


def test_get_session_token(sts_get_session_response, sts_get_caller_id_response):
    sts = MagicMock()
    sts.get_session_token.return_value = sts_get_session_response
    sts.get_caller_identity.return_value = sts_get_caller_id_response

    assert get_sesion_token(sts, "user", "000000") == sts_get_session_response


def test_get_session_token_fail(
    sts_get_session_response, sts_get_caller_id_response, sts_get_session_error
):
    sts = MagicMock()
    sts.get_session_token = MagicMock(
        side_effect=ClientError(sts_get_session_error, "Error")
    )
    sts.get_caller_identity.return_value = sts_get_caller_id_response

    with pytest.raises(ClientError) as error:
        get_sesion_token(sts, "user", "000000")
    assert "WhatEver" in str(error.value)
