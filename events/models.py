from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class events(models.Model):
    # organiser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=150, unique=True)
    venue = models.CharField(max_length=150, unique=True)
    venue_image = CloudinaryField('image', default='placeholder')
    event_date = models.DateField('Event Date', blank=True, null=True)
    guest_limit = models.IntegerField('Guest limit',
                                        default=0,
                                        choices=[(0, u"No limit")] + list(zip(range(1,100), range(1,100))))
    description = models.TextField(blank=True, max_length=200)
    approve = models.BooleanField(default=False)


    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = "Event"

# class User_Count(models.Model):
#     Guests_attending = models.ManyToManyField(
#         User, related_name='events_guests', blank=True)


#     def num_of_users_attending(self):
#         return self.Guests_attending.count()
