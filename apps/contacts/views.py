from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from apps.contacts.forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contacts:submitted')

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name').capitalize()
        last_name = form.cleaned_data.get('last_name').capitalize()
        email = form.cleaned_data.get('email').casefold()
        message = form.cleaned_data.get('message')
        send_mail(
            subject=f"Contact Form - from {first_name} {last_name}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL_SES,
            recipient_list=['contact@waynelambert.dev', email],
            fail_silently=False,
        )
        form.save()
        return super().form_valid(form)


class ContactSubmittedView(TemplateView):
    template_name = 'contact_submitted.html'
