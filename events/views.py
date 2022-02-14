from . import views
from django.views import generic, View
from blog.models import User
from datetime import datetime
from django.http import HttpResponseRedirect
from .forms import EventForm

# Create your views here.

class EventList(generic.ListView):
        queryset = Post.objects.filter(status=1).order_by("-created_on")
        template_name = "events.html"
        paginate_by = 6
        # upcoming = Event.objects.filter(date__gte=now).order_by('date')
        # passed = Event.objects.filter(date__lt=now).order_by('-date')
        # return list(upcoming) + list(passed)

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = EventForm
            if 'submitted' in request.POST:
                submitted = True

        return render(request, 'add_event.html', {'form':form, 'submitted':submitted})


