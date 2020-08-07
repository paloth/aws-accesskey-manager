from click.testing import CliRunner
from akm import main
from unittest.mock import patch


@patch("akm.cmd.cmdMfa.boto3")
def test_mfa_execution(mock_boto3, tmpdir, fake_profile, sts_get_session_response, sts_get_caller_id_response):
    p = tmpdir.mkdir(".aws").join("credentials")
    p.write(fake_profile)
    with patch("akm.main.AWS_PROFILE_FILE", p):
        runner = CliRunner()
        runner.invoke(main.run, ["mfa", "-u", "test", "-t", "000000", "-p", "test"])

        assert p.read() == "[test]\n" + "aws_access_key_id = AKEXAMPLE\n" + "aws_secret_access_key = SKEXAMPLE"
    # assert "Profile [test-tmp] has been updated and will expire on 01/01/2020 00:00:00}" in result.output
