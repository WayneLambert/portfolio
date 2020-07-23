""" Countdown Letters: Oxford API

A collection of objects that handles the external interface with the
Oxford Dictionary API.

Dev Guide: https://developer.oxforddictionaries.com/documentation
"""

import os


class API:
    """
    Handles the API configuration for the Online Oxford Dictionary API.
    """
    headers = {
        "Accept": "application/json",
        "app_id": os.environ['OD_APPLICATION_ID'],
        "app_key": os.environ['OD_APPLICATION_KEY_1'],
    }
    ENTRIES_URL = f"{os.environ['OD_API_BASE_URL']}{'entries/en-gb/'}"
    LEMMAS_URL = f"{os.environ['OD_API_BASE_URL']}{'lemmas/en-gb/'}"
    WORDS_URL = f"{os.environ['OD_API_BASE_URL']}{'words/en-gb'}"
