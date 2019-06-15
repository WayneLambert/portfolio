from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import Category, Post


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-publish_date'),
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-publish_date']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-publish_date']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user, status=1).order_by('-publish_date')


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    ordering = ['-publish_date']
    paginate_by = 3

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(categories=self.category, status=1)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['categories'] = self.category
        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


"""
The code below is for an API implementation of the blog using serializers as
opposed to views.
"""

# from rest_framework import viewsets
# from blog.models import Post
# from blog.serializers import PostSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
