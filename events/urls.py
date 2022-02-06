from . import views
from django.urls import path, include


urlpatterns = [
    path('events/', views.events, name='events'),
]
