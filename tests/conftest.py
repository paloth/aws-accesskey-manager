from pytest import fixture
from datetime import datetime
from dateutil.tz import tzutc


@fixture()
def fake_profile():
    return "[test]\n" + "aws_access_key_id = AKEXAMPLE\n" + "aws_secret_access_key = SKEXAMPLE"


@fixture()
def fake_config():
    return {"test": {"aws_access_key_id": "", "aws_secret_access_key": "", "aws_default_region": ""}}


@fixture()
def sts_get_session_response():
    return {"Credentials": {"AccessKeyId": "accesskey", "SecretAccessKey": "secretkey", "SessionToken": "sessiontoken"}}


@fixture()
def sts_get_caller_id_response():
    return {"UserId": "string", "Account": "000000000000", "Arn": "string"}


@fixture()
def iam_list_ak_response():
    return {"AccessKeyMetadata": [{"AccessKeyId": "AKIA111111111EXAMPLE"}, {"AccessKeyId": "AKIA222222222EXAMPLE"}]}


@fixture()
def iam_create_access_key_return():
    return {"AccessKey": {"AccessKeyId": "accesskey", "SecretAccessKey": "secretkey"}}


@fixture()
def boto_standard_error():
    return {"Error": {"Code": "WhatEver", "Message": "Error"}}


@fixture()
def sts_get_session_error():
    return {"Error": {"Code": "WhatEver", "Message": "Error"}}


@fixture()
def iam_limit_exceeded_exception():
    return {"Error": {"Code": "LimitExceededException", "Message": "Error"}}


@fixture()
def current_mocked_date():
    return datetime(2020, 7, 1, 10, 00, 00, tzinfo=tzutc())


@fixture()
def creation_mocked_date():
    return datetime(2020, 5, 1, 10, 00, 00, tzinfo=tzutc())
