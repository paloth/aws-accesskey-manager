from click.testing import CliRunner
from src.main import run
from unittest.mock import patch


def test_mfa_execution(tmpdir, fake_profile):
    p = tmpdir.mkdir(".aws").join("credentials")
    p.write(fake_profile)
    with patch("src.main.AWS_PROFILE_FILE", p):
        runner = CliRunner()
        runner.invoke(run, ["mfa", "-u", "test", "-t", "000000", "-p", "test"])

        assert p.read() == "[test]\n" + "aws_access_key_id = AKEXAMPLE\n" + "aws_secret_access_key = SKEXAMPLE"
    # assert "Profile [test-tmp] has been updated and will expire on 01/01/2020 00:00:00}" in result.output
