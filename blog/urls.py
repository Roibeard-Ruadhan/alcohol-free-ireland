from django.urls import path
from .views import HomeView

urlpatterns = [
    path(BlogList.as_view(), name="blog"),
]
