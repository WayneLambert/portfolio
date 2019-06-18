from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def view_cv(request):
    return render(request, 'cv.html')


def about_blog(request):
    return render(request, 'about_blog.html')


def contact_form(request):
    return render(request, 'contact.html')
