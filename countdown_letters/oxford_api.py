import os


class API:
    OD_API_BASE_URL = os.environ['OD_API_BASE_URL']
    OD_APPLICATION_ID = os.environ['OD_APPLICATION_ID']
    OD_APPLICATION_KEY_1 = os.environ['OD_APPLICATION_KEY_1']
    LANGUAGE = 'en-gb'
    headers = {
        "app_id": OD_APPLICATION_ID,
        "app_key": OD_APPLICATION_KEY_1,
    }
