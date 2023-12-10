from django import forms

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email", "message")

    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                "data-theme": "light",
                "data-size": "invisible",
            },
        )
    )
