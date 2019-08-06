from django.shortcuts import render, redirect

AWS_BUCKET_ADDRESS = 'https://wl-portfolio.s3.eu-west-2.amazonaws.com/'

def about_me(request):
    return render(request, 'about_me.html')

def contact_form(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def reading_list(request):
    return render(request, 'reading_list.html')

def view_cv(request):
    return redirect(AWS_BUCKET_ADDRESS + 'documents/cv_wayne_lambert.pdf')
