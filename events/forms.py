from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
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
        'location': froms.TextInput(attrs={''})
        'venue': froms.TextInput(attrs={''})
        'event_date': froms.Date Input(attrs={''})
        'description': froms.TextInput(attrs={''})
        'attendees_number': froms.NumberInput(attrs={''})
    }

