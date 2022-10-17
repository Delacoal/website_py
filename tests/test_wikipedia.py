from my_hypermodern_python import wikipedia
from my_hypermodern_python.wikipedia import Page


def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(language="en")
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get):
    page = wikipedia.random_page(language="en")
    assert isinstance(Page, wikipedia.page)
