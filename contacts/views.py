from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from contacts.forms import ContactForm


def contact(request):
    contact_form_template = 'contacts/contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            send_mail(
                subject='Contact Form',
                message=request.POST['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['contact@waynelambert.dev'],
                fail_silently=False
            )
            return redirect('contact-submitted')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, contact_form_template, context)


def contact_submitted(request):
    return render(request, 'contact_submitted.html')
