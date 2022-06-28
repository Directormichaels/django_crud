from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'Post_list.html'

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    template_name = 'Post_form.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'Post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = 'Post_update.html'

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = 'Post_delete.html'