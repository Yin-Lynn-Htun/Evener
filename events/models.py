from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    date = models.DateField()
    registered = models.IntegerField(default=0)
    organizer = models.CharField(max_length=100, default='Maung Maung')
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name 