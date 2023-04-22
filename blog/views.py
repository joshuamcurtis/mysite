from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('home')
    form_class = PostForm

class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-published_date')
    template_name = 'blog\index.html'
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog\post_detail.html'
