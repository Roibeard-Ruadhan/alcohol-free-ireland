from django.db import models

# Create your models here.
class Event(models.Model):
    location = models.CharField('location', max_length=150)
    venue = models.CharField('Event Venue', max_length=150)
    event_date = models.DateTimeField('Event Time')
    guest_limit = models.IntegerField('Guest limit',
                                        default=0,
                                        choices=[(0, u"No limit")] + list(zip(range(1,100), range(1,100))))
    description = models.TextField(blank=True, max_length=200)


    # user_name = models.ManyToManyField(?)

    def __str__(self):
        return self.name
