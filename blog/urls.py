from django.urls import path
from django.conf.urls import * 
from .views import BlogList, ArticleDetail, index

urlpatterns = ['',
    url(r'^$', views.index, name='index'),
    path(BlogList.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),

]
