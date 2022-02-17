from . import views
from django.urls import path


urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('add_event/', views.add_event, name='add-event'),
]
