import requests
import click

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"

error_test = "https://httpbin.org/status/404"


def random_page(language="en"):
    URL = API_URL.format(language=language)

    try:
        with requests.get(URL) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
