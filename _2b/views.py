from django.shortcuts import get_object_or_404, render


def home(request):
    return render(request, 'home.html')
