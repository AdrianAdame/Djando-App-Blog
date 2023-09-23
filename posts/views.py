from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post

#The update view class requires at a minimum:
#   1. Template name
#   2. Model
#   3. List of fields that should be present on the generated form

#The update view will require a very specific url pattern which should include
# the primary key of the instance of our model that we wish to modify

# The delete view will also require a primary key to be prvided a url pattern

# The delete view will need, at minimum:
#1. template_name
#2. model
#3. success_url (this should be redirect our users after a successful delete)

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "author"]

class PostUpdateView(UpdateView):
    template_name = "posts/update.html"
    model = Post
    fields = ["title", "subtitle", "body", "author"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy('list')