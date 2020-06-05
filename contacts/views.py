from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm


def contact(request):
    contact_form_template = 'contacts/contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            full_name = f"{request.POST['first_name'].strip()} {request.POST['last_name'].strip()}"
            sender_email = request.POST['email'].strip()
            send_mail(
                subject=f'Contact Form - from {full_name}',
                message=request.POST['message'],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['contact@waynelambert.dev', sender_email],
                fail_silently=False
            )
            return redirect('contacts:contact_submitted')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, contact_form_template, context)


def contact_submitted(request):
    return render(request, 'contacts/contact_submitted.html')
