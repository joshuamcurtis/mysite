from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

'''
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'author']
    success_url = ''
'''
class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-published_date')
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
