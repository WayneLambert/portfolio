from bs4 import BeautifulSoup
import requests


# TODO: Refactor BS4 and requests section within master function into here
def get_parsed_letters_selected():
    URL = request.get_full_path
    page_response = requests.get(URL, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    letters = page_content.find(
        "div", {"class": "letters-selected"}).text
    letters = letters.replace('\n', '').replace('              ', '').strip()
    return letters

parsed_letters = get_parsed_letters_selected()

print(parsed_letters)
