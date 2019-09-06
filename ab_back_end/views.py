from django.shortcuts import render, redirect
from ab_back_end.settings import AWS_REACT_BUCKET_LOCATION

AWS_BUCKET_ADDRESS = 'https://wl-portfolio.s3.eu-west-2.amazonaws.com/'
AWS_DOCUMENTS_FOLDER = 'documents/'
AWS_CV_FILENAME = 'cv_wayne_lambert.pdf'


def home(request):
    return render(request, 'home.html')

def contact_form(request):
    return render(request, 'contact.html')

def reading_list(request):
    return render(request, 'reading_list.html')

def view_cv(request):
    return redirect(f'{AWS_BUCKET_ADDRESS}{AWS_DOCUMENTS_FOLDER}{AWS_CV_FILENAME}')

def about_me(request):
    return render(request, 'about_me.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def react_blog(request):
    return redirect(AWS_REACT_BUCKET_LOCATION)
