# src/hypermodern_bersten/wikipedia.py
import requests

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language):

    global API_URL

    if not language == "en":
        API_URL = API_URL.replace("en", str(language), 1)

    with requests.get(API_URL) as response:
        response.raise_for_status()
        return response.json()

    # with requests.get(API_URL) as response:
    #     try:
    #         response.raise_for_status()
    #         data = response.json()
    #     except requests.exceptions.RequestException as e:
    #         raise SystemExit(e)
