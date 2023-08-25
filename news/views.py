from typing import Any, Dict
from django.views.generic import ListView, DetailView
from .models import Post, Author, User
from datetime import datetime


# Create your views here.
class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news/posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'

class AuthorList(ListView):
    model = Author  # указываем модель, объекты которой мы будем выводить
    template_name = 'news/authors.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'authors'
    queryset = Author.objects.order_by('-id')

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class AuthorDetail(DetailView):
    model = User
    template_name = 'news/author.html'
    context_object_name = 'author'
