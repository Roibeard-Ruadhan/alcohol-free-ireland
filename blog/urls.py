"""Blog Urls"""
from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.Homepage, name="home"),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('events/', include('events.urls'), name='events-urls'),
    path('contact/', views.contact, name='contact'),
    path('add_blog/', views.create_post, name='add_blog'),
    path('edit_blog/<int:blog_post_id>/', views.edit_blog, name='edit_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
