from django import forms

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')

    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'data-theme': 'light',
                'data-size': 'invisible',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
