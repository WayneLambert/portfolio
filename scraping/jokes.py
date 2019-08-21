from django.shortcuts import render
import requests

def get_joke(request):
    url = "https://icanhazdadjoke.com/"

    response = requests.get(url, headers={"Accept": "application/json"})
    joke = response.json()['joke']

    return render(request, 'jokes.html', {'joke': joke})
