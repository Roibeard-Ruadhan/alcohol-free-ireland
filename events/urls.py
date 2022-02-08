from . import views
from django.urls import path


urlpatterns = [
    path('events/', views.events.as_view(), name='events'),
    path('add_events/', views.events.as_view(), name='add-events'),
]
