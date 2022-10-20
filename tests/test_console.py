from unittest.mock import Mock

import click.testing
import pytest
import requests
from click.testing import CliRunner
from pytest_mock import MockFixture

from my_hypermodern_python import console


@pytest.fixture
def runner() -> CliRunner:
    return click.testing.CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture):
    return mocker.patch("my_hypermodern_python.wikipedia.random_page")


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner: CliRunner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_requests_get):
    """Test if console.main prints Title"""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(runner, mock_requests_get):
    """mocks can be inspected to see if they were called,
    using the mock's called attribute. This provides you
    with a way to check that requests.get was invoked to
    send a request to the API:"""
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


def test_main_fails_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output
