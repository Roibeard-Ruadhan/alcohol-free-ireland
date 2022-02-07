from . import views
from django.views import generic, View
from blog.models import User
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EventForm

# Create your views here.

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = EventForm
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})


# class events(View):
#     def events(request):
#         return render(request, 'add_events.html')
