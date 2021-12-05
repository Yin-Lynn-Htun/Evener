from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.street

class Organizer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return self.name 