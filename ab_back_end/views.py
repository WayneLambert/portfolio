from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, render_to_response, redirect

def home(request):
    return render(request, 'home.html')


def view_cv(request):
    return redirect('https://wl-portfolio.s3.eu-west-2.amazonaws.com/documents/cv_wayne_lambert.pdf')


def contact_form(request):
    return render(request, 'contact.html')
