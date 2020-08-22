"""
Retrieves the Gettysburg address from the goodreads.com website removing
any new line escape and other extraneous characters returned from the
parsed HTML.
"""

from django.shortcuts import render

# pylint: disable=invalid-name
import requests

from bs4 import BeautifulSoup


def get_gettysburg_speech(request):
    URL = "https://www.goodreads.com/work/quotes/4694-the-illustrated-gettysburg-address"
    page_response = requests.get(URL, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    text_content, split_string = [], []
    for num in range(2):
        paragraphs = page_content.find_all('div', attrs={"class": "quoteText"})[num].text
        text_content.append(paragraphs)
    split_string = text_content[1].strip('\n').strip().split('\n')
    gettysburg_speech = split_string[0]

    context = {'gettysburg': gettysburg_speech}

    return render(request, 'gettysburg_speech.html', context)
