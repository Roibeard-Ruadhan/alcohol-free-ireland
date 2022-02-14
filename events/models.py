from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class events(models.Model):
    # organiser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=150, unique=True)
    venue = models.CharField(max_length=150, unique=True)
    event_date = models.DateTimeField('Event Time')
    guest_limit = models.IntegerField('Guest limit',
                                        default=0,
                                        choices=[(0, u"No limit")] + list(zip(range(1,100), range(1,100))))
    description = models.TextField(blank=True, max_length=200)


    # user_name = models.ManyToManyField(?)

    def __str__(self):
        return self.location

