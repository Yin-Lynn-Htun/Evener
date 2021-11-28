from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Event

# Create your views here.


def index(request):
    return render(request, 'events/index.html' )

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html' , {'events' : events})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    # try:
    #     event = Event.objects.get(id=id)
    # except:
    #     raise Http404()
    return render(request, 'events/event_detail.html' , {'event': event})