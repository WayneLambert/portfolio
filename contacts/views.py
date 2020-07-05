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
            cleaned_first_name = form.cleaned_data['first_name'].title()
            cleaned_last_name = form.cleaned_data['last_name'].title()
            full_name = f"{cleaned_first_name} {cleaned_last_name}"
            cleaned_email = form.cleaned_data['email'].casefold()
            cleaned_message = form.cleaned_data['message']
            send_mail(
                subject=f"Contact Form - from {full_name}",
                message=cleaned_message,
                from_email=settings.DEFAULT_FROM_EMAIL_SES,
                recipient_list=['contact@waynelambert.dev', cleaned_email],
                fail_silently=False
            )
            return redirect('contacts:submitted')
    else:
        form = ContactForm()

    context = {'form': form}

    return render(request, contact_form_template, context)


def contact_submitted(request):
    return render(request, 'contacts/contact_submitted.html')
