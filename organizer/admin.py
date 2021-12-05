from django.contrib import admin
from .models import Address, Organizer

# Register your models here.
admin.site.register(Organizer)
admin.site.register(Address)