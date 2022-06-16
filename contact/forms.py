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



# class ContactForm(forms.Form):
#     yourname = forms.CharField(max_length=100, label='Your Name')
#     email = forms.EmailField(required=False, label='Your Email Address')
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
