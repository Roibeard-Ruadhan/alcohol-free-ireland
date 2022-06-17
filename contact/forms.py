from django import forms
from .models import Contact_mails


class ContactForm(forms.ModelForm):
    """
    Creates a contact form
    """
    class Meta:
        model = Contact_mails

        fields = ('full_name', 'email', 'subject', 'message',)
