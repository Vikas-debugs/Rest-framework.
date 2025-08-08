# your_app/forms.py

from captcha.fields import CaptchaField
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # Add the CaptchaField
    captcha = CaptchaField()
