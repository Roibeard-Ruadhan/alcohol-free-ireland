from django.urls import path
from .views import BlogList, ArticleDetail
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("blog/", BlogList.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
]
