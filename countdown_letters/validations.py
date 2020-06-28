import os

import requests


def is_in_oxford_api(word: str) -> bool:
    OD_API_BASE_URL = os.environ['OD_API_BASE_URL']
    OD_APPLICATION_ID = os.environ['OD_APPLICATION_ID']
    OD_APPLICATION_KEY_1 = os.environ['OD_APPLICATION_KEY_1']
    LANGUAGE = 'en-gb'
    headers = {
        "app_id": OD_APPLICATION_ID,
        "app_key": OD_APPLICATION_KEY_1,
    }
    url = f'{OD_API_BASE_URL}{"lemmas/"}{LANGUAGE}{"/"}{word.lower()}'
    response = requests.get(url, headers=headers)
    return response.status_code == 200


def is_eligible_answer(answer: str, letters: str) -> bool:
    letters_in_answer = list(answer)
    letters_in_selection = list(letters)
    while letters_in_answer:
        for letter in answer:
            if letter in letters_in_answer and letter in letters_in_selection:
                letters_in_selection.remove(letter)
                letters_in_answer.remove(letter)
            else:
                return False
        return True
