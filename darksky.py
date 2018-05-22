from typing import Dict

import requests


def get_today_weather(apikey, location):
    """

    :param apikey: A valid darksky.net API key.
    :param location: A location in latitude,longitude format.
    :return: A dictionary containing today's projected weather.
    """

    payload: Dict[str, str] = {'exclude': 'currently,minutely,hourly'}
    url = f'https://api.darksky.net/forecast/{apikey}/{location}'
    scrape = requests.get(url, params=payload)
    scrape.raise_for_status()

    forecast = scrape.json()['daily']['data'][0]
    return forecast
