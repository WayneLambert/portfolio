from bs4 import BeautifulSoup
from django.shortcuts import render
import requests
# pylint: disable=invalid-name

URL = "https://www.goodreads.com/work/quotes/4694-the-illustrated-gettysburg-address"

# Fetch the content from the url, using the requests library
page_response = requests.get(URL, timeout=5)

# Parse the url content
page_content = BeautifulSoup(page_response.content, "html.parser")

def get_gettysburg_speech(request):
    """
    Retrieves the Gettysburg address from the goodreads.com website removing
    any new line escape characters returned from the parsed HTML.
    """
    text_content = []
    split_string = []
    for i in range(0, 2):
        paragraphs = page_content.find_all('div',
                                           attrs={"class": "quoteText"})[i].text
        text_content.append(paragraphs)
    split_string = text_content[1].strip('\n').strip().split('\n')
    gettysburg_speech = split_string[0]
    return render(
        request,
        'gettysburg_speech.html',
        {'gettysburg': gettysburg_speech}
    )
