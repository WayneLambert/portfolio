from django.shortcuts import render


def speech_list(request):
    return render(request, 'scraping/speech-list.html')
