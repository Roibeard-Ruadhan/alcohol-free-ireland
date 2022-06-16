from django import forms
from .models import Contact_emails


class ContactForm(forms.ModelForm):
    """
    Creates a contact form
    """
    class Meta:
        model = Contact_emails

        fields = (
            'full_name',
            'email',
            'subject',
            'message',
        )
