from bs4 import BeautifulSoup
import requests
from django.shortcuts import render


url = "https://www.goodreads.com/quotes/55276-i-have-nothing-to-offer-but-blood-toil-tears-and"
page_response = requests.get(url, timeout=5)

# Fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")

# Use the html parser to parse the url content and store it in a variable.


def get_churchill_speech(request):
    """Retrieves Winston Churchill's first speech as UK prime minister from goodreads.com"""
    speech_text = str(page_content.findChildren('h1')).split('\n')[1].split(';<br/>')[0].strip() + '."'
    return render(request, 'scraping/churchill_speech.html', {'churchill_speech': speech_text})
