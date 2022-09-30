from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from .models import Post

# class PostHome(HomePageView):
#     template_name = "posts/home.html"
#     model = Post
class HomePageView(TemplateView): # Instantiates a new TemplateView class
    template_name = "posts/home.html"

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

