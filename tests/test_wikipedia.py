"""Test cases for the wikipedia module."""
from unittest.mock import Mock

import click
from hypermodern_bersten import wikipedia
import pytest


def test_main_uses_custom_wikipedia_org(mock_requests_get: Mock) -> None:
    """It selects the specified Wikipadia language edition."""
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get: Mock) -> None:
    """It returns a page."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    """It raises `ClickException` when validation fails."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()


def test_trigger_typeguard(mock_requests_get: Mock) -> None:
    """It triggers typeguard for invalid input."""
    import json

    data = json.loads('{ "language": 1 }')
    wikipedia.random_page(language=data["language"])
