import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# pylint: disable=invalid-name


def get_churchill_speech(request):
    """
    Retrieves Winston Churchill's first speech as UK prime minister from the goodreads.com
    website removing any new line escape characters returned from the parsed HTML.
    """

    URL = "https://www.goodreads.com/quotes/55276-i-have-nothing-to-offer-but-blood-toil-tears-and"
    page_response = requests.get(URL, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    churchill_speech = str(
        page_content.findChildren('h1')).split('\n')[1].split(';<br/>')[0].strip() + '."'

    context = {'churchill_speech': churchill_speech}

    return render(request, 'churchill_speech.html', context)