from django.shortcuts import render


def speech_list(request):
    return render(request, 'speech-list.html')
