from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class events(models.Model):
    # organiser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=150, unique=False)
    venue = models.CharField(max_length=150, unique=False)
    venue_image = CloudinaryField('image', default='placeholder')
    event_date = models.DateField('Event Date', blank=True, null=True)
    description = models.TextField(blank=True, max_length=200)
    approve = models.BooleanField(default=False)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events_creator", null=True
    )
    guests = models.ManyToManyField(
        User, related_name='events_guests', blank=True)

    def number_of_guests(self):
        return self.guests.count()
    def __str__(self):
        return self.location


    # Events plural in the admin
    class Meta:
        verbose_name_plural = "Event"
   
   
    # def __str__(self):
     #     return self.events


# class User_Count(models.Model):
#     Guests_attending = models.ManyToManyField(
#         User, related_name='events_guests', blank=True)


#     def num_of_users_attending(self):
#         return self.Guests_attending.count()
