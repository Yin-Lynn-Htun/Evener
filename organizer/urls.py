from django.urls import path
from . import views

urlpatterns = [
    path('' , views.organizer_list, name = 'organizer_list'),
    path('<int:id>/' , views.organizer_detail, name='organizer_detail')
]
