from django.db import models

from Evener.settings import BASE_DIR
from organizer.models import Organizer
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    date = models.DateField()
    registered = models.IntegerField(default=0)
    organizer = models.ForeignKey( Organizer, on_delete=models.CASCADE, null=True)
    detail = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="event_img", null=True)

    def __str__(self):
        return self.name 

    # pip -m install pillow