from dataclasses import dataclass

import click
import requests
import desert
import marshmallow


API_URL: str = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"

error_test = "https://httpbin.org/status/404"


@dataclass
class Page:
    title: str
    extract: str


schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})


def random_page(language: str = "en") -> Page:
    URL = API_URL.format(language=language)

    try:
        with requests.get(URL) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message) from error
