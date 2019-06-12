from bs4 import BeautifulSoup
import requests
from django.shortcuts import render


url = "https://www.goodreads.com/work/quotes/4694-the-illustrated-gettysburg-address"
page_response = requests.get(url, timeout=5)

# Fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")


# Use the html parser to parse the url content and store it in a variable.
def get_gettysburg_speech(request):
    """ Retrieves the Gettysburg address from the goodreads.com website. """
    textContent = []
    split_string = []
    for i in range(0, 2):
        paragraphs = page_content.find_all('div',
                                           attrs={"class": "quoteText"})[i].text
        textContent.append(paragraphs)
    split_string = textContent[1].strip('\n').strip().split('\n')
    gettysburg_speech = split_string[0]
    return render(request, 'gettysburg_speech.html',
                  {'gettysburg': gettysburg_speech}
    )
