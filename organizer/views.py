from django.shortcuts import get_object_or_404, render
from .models import Organizer

# Create your views here.
def organizer_list(request):
    organizers = Organizer.objects.all()
    return render(request, 'organizer/organizer_list.html' , {'organizers': organizers})

def organizer_detail(request, id):
    organizer = get_object_or_404(Organizer, id = id)
    return render(request, 'organizer/organizer_detail.html', {'organizer': organizer})