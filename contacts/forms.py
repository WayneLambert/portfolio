from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'data-theme': 'light',
                'data-size': 'invisible',
            }
        )
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize().strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].capitalize().strip()

    def clean_email(self):
        return self.cleaned_data['email'].casefold().strip()

    def clean_message(self):
        return self.cleaned_data['message'].casefold().strip()

    def full_name(self):
        return f"{self.clean_first_name} {self.clean_last_name}"
