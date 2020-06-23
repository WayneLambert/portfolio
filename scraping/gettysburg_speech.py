from bs4 import BeautifulSoup
from django.shortcuts import render
import requests
# pylint: disable=invalid-name


def get_gettysburg_speech(request):
    """
    Retrieves the Gettysburg address from the goodreads.com website removing
    any new line escape characters returned from the parsed HTML.
    """

    URL = "https://www.goodreads.com/work/quotes/4694-the-illustrated-gettysburg-address"
    page_response = requests.get(URL, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    text_content = []
    split_string = []
    for i in range(2):
        paragraphs = page_content.find_all('div', attrs={"class": "quoteText"})[i].text
        text_content.append(paragraphs)
    split_string = text_content[1].strip('\n').strip().split('\n')
    gettysburg_speech = split_string[0]
    return render(
        request,
        'gettysburg_speech.html',
        {'gettysburg': gettysburg_speech}
    )
