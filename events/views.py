from . import views
from django.shortcuts import render
from django.views import generic, View
from blog.models import User

# Create your views here.
class events(View):
    def events(request):
        return render(request, 'add_events.html')
