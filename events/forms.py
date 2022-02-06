from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'location', 'event_date', 'description' 'attendees_number')
        labels = {
            'location': '',
            'venue': '',
            'event_date': '',
            'description': '',
            'attendees_number': '',
        }
        widgets = {
            'location': froms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'})
            'venue': froms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue'})
            'event_date': froms.Date Input(attrs={'class':'form-control', 'placeholder':'Event Date'})
            'description': froms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'})
            'attendees_number': froms.NumberInput(attrs={'class':'form-control', 'placeholder':'Maximum number that can attend'})
        }

