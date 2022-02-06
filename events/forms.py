from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'location', 'event_date', 'attendees_number', 'description')
        labels = {
            'location': 'County/Town',
            'venue': 'Venue',
            'event_date': 'Event Date',
            'attendees_number': 'Max Attendees',
            'description': 'Description',
        }
        widgets = {
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'venue': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue'}),
            'event_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
            'attendees_number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Maximum number that can attend'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        }

