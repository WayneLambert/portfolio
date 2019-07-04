from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def view_cv(request):
    fs = FileSystemStorage()
    cv_filename = 'cv_wayne_lambert.pdf'
    if fs.exists(cv_filename):
        with fs.open(cv_filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=cv_filename'
            return response
    else:
        return HttpResponseNotFound('The CV was not found in the server.')


def contact_form(request):
    return render(request, 'contact.html')


def error_404(request, exception):
    return render(request, 'templates/404.html')
