from unittest.mock import patch
from akm.internal import aws_config
import configparser


def test_get_config(tmpdir, fake_profile):
    path = tmpdir.mkdir(".aws").join("credentials")
    path.write(fake_profile)

    with patch("akm.main.AWS_PROFILE_FILE", path):
        assert isinstance(aws_config.get(path), configparser.ConfigParser)


def test_get_profile_ak(tmpdir, fake_profile):
    path = tmpdir.mkdir(".aws").join("credentials")
    path.write(fake_profile)

    config = aws_config.get(path)

    assert aws_config.get_profile_ak_id("test", config) == "AKEXAMPLE"


def test_write_config(tmpdir, fake_profile, sts_get_session_response):
    path = tmpdir.mkdir(".aws").join("credentials")
    path.write(fake_profile)

    config = aws_config.get(path)

    aws_config.write(path, "test", config, sts_get_session_response)

    assert config.has_section("test-tmp") is True
    assert config.get("test-tmp", "aws_access_key_id") == "accesskey"
    assert config.get("test-tmp", "aws_secret_access_key") == "secretkey"
    assert config.get("test-tmp", "aws_session_token") == "sessiontoken"


def test_update_config(tmpdir, fake_profile, iam_create_access_key_return):
    path = tmpdir.mkdir(".aws").join("credentials")
    path.write(fake_profile)

    config = aws_config.get(path)

    aws_config.update_profile(path, "test", config, iam_create_access_key_return)

    assert config.has_section("test") is True
    assert config.get("test", "aws_access_key_id") == "accesskey"
    assert config.get("test", "aws_secret_access_key") == "secretkey"
