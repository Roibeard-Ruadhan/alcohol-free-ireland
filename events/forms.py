from django import forms
from django.forms import ModelForm
from .models import events

class EventForm(ModelForm):
    class Meta:
        model = events
        fields = ('location', 'venue', 'event_date', 'guest_limit', 'description')
        labels = {
            'location': 'County/Town',
            'venue': 'Venue',
            'event_date': 'Event Date',
            'guest_limit': 'Max Attendees',
            'description': 'Description',
        }
        widgets = {
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'venue': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue'}),
            'event_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
            'guest_limit': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Maximum number that can attend'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Arrival time & other details'}),
        }