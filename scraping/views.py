from django.shortcuts import render


def scraping_options_list(request):
    return render(request, 'scraping/scraping_options.html')
