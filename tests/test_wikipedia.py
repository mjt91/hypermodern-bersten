# tests/test_wikipedia.py
from hypermodern_bersten import wikipedia


def test_main_uses_custom_wikipedia_org(mock_requests_get):
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]
