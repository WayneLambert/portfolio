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
            send_mail(
                subject=f"Contact Form - from {ContactForm.full_name}",
                message=ContactForm.clean_message,
                from_email=settings.DEFAULT_FROM_EMAIL_SES,
                recipient_list=['contact@waynelambert.dev', ContactForm.clean_email],
                fail_silently=False
            )
            return redirect('contacts:submitted')
    else:
        form = ContactForm()

    context = {'form': form}

    return render(request, contact_form_template, context)


def contact_submitted(request):
    return render(request, 'contacts/contact_submitted.html')
