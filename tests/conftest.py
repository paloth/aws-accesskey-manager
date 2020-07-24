from pytest import fixture


@fixture()
def sts_get_session_response():
    return {
        "Credentials": {
            "AccessKeyId": "accesskey",
            "SecretAccessKey": "secretkey",
            "SessionToken": "sessiontoken",
        }
    }


@fixture()
def sts_get_caller_id_response():
    return {"UserId": "string", "Account": "000000000000", "Arn": "string"}


@fixture()
def sts_get_session_error():
    return {"Error": {"Code": "WhatEver", "Message": "Error"}}
