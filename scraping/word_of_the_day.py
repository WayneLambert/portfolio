import textwrap
import re
import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

def get_word_of_the_day(request):
    URL = 'https://www.dictionary.com/e/word-of-the-day/'
    page_response = requests.get(URL, timeout=5, allow_redirects=False)

    if page_response.status_code == 200:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        word = page_content.select(".wotd-item__definition h1")
        word = str(word[0]).replace("<h1>", '').replace("</h1>", '')
        definition = page_content.select(".wotd-item__definition__text")
        definition = str(definition[0]).replace('<div class="wotd-item__definition__text">', '')
        definition = textwrap.dedent(definition.replace("</div>", '')).strip()
        definition = re.sub('<[^>]+>', '', definition)
        print(f"{'Word of the Day: '}{word}")
        print(f"{'Definition: '}{definition}")
    else:
        print(f"{'There was no response for the URL of'} {URL}")

    context = {
        'word': word,
        'definition': definition,
    }

    return render(
        request,
        'word_of_the_day.html',
        {'context': context}
    )
