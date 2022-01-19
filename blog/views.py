from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Post

def index(request):
    return render(request, '/index.html')

class BlogList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6

class ArticleDetail(DetailView):
    model = Post()
    template_name = 'article_detail.html'