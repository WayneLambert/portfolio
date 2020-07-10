from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView

from .forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contacts/contact.html'

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        send_mail(
            subject=f"Contact Form - from {first_name} {last_name}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL_SES,
            recipient_list=['contact@waynelambert.dev', email],
            fail_silently=False,
        )
        return super(ContactFormView, self).form_valid(form)


class ContactSubmittedView(TemplateView):
    template_name = 'contact_submitted.html'
