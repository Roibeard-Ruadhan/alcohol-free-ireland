from django.urls import path
from django.conf.urls.defaults import * 
from .views import BlogList, ArticleDetail

urlpatterns = [
    path(BlogList.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),

]
