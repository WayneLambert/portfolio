from django import forms
from captcha.fields import CaptchaField
from contacts.models import Contact


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')
