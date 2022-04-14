from pathlib import Path

from click.testing import CliRunner

from openldap_config_parser.command import cli

BASE_DIR = Path(__file__).parent


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0


def test_cli_dry_run():
    success_conf = Path(BASE_DIR, "config", "simple_slapd.conf")
    runner = CliRunner()
    result = runner.invoke(cli, ["--dry-run", str(success_conf)])
    assert result.exit_code == 0
