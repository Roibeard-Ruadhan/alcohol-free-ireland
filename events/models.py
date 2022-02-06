from django.db import models

# Create your models here.
class Event(models.Model):
    location = models.CharField(max_length=45)
    Venue = models.Charfield('Event Venue')
    event_date = models.DateTimeField('Event Time')
    description = models.TextField(blank=True, max_length=200)
    attendees_number = models.ManyToManyField('Users Attending')
    # user_name = models.ManyToManyField(?)

    def __str__(self):
        return self.name
