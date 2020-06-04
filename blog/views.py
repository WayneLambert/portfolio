from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import PostForm
from .models import Category, Post


class HomeView(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-publish_date')
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 6
    extra_context = {'categories_list': Category.objects.all()}


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6
    extra_context = {'categories_list': Category.objects.all()}

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user, status=1).order_by('-publish_date')


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 6
    extra_context = {'categories_list': Category.objects.all()}

    def get_queryset(self):
        self.categories = get_list_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(categories=self.categories[0].id)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        return context


class PostDetailView(DetailView):
    model = Post
    extra_context = {'categories_list': Category.objects.all()}


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

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
    template_name = 'post_components/post_confirm_delete.html'
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    extra_context = {'categories_list': Category.objects.all()}

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class ContentsListView(ListView):
    model = Category
    template_name = 'blog/posts_list.html'

    def get_context_data(self, **kwargs):
        context = super(ContentsListView, self).get_context_data(**kwargs)
        categories_list = Category.objects.all().order_by('name')
        categories = Category.objects.all().order_by('name')
        posts = Post.objects.filter(status=1).order_by('-publish_date')
        context = {
            'categories_list': categories_list,
            'categories': categories,
            'posts': posts,
        }
        return context
