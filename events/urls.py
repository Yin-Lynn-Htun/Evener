from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:id>/' , views.event_detail, name='event_detail')
]
