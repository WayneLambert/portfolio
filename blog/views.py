from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import PostForm
from .models import Category, Post


class PostView(ListView):
    """ Custom View to set behaviour of all list views for the blog. """
    model = Post
    context_object_name = 'posts'
    category_list = Category.objects.all().prefetch_related('posts')
    extra_context = {'categories_list': category_list}
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')


class HomeView(PostView):
    """ View to drive the list of posts on the blog's home page. """
    template_name = 'blog/home.html'
    paginate_by = 6


class UserPostListView(PostView):
    """ View to drive the list of posts on an author's blog posts page. """
    template_name = 'blog/user_posts.html'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        qs = self.queryset.filter(author=user, status=1)
        return qs


class CategoryPostListView(PostView):
    """ View to drive the list of posts for any given category. """
    template_name = 'blog/category_posts.html'
    paginate_by = 6

    def get_queryset(self):
        self.categories = get_list_or_404(Category, slug=self.kwargs['slug'])
        qs = self.queryset.filter(categories=self.categories[0].id)
        return qs

    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        return context


class PostDetailView(DetailView):
    """ View to drive the list of posts for any given category. """
    model = Post
    category_list = Category.objects.all().prefetch_related('posts')
    extra_context = {'categories_list': category_list}


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
        if self.request.user.id == post.author.id:
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


class SearchResultsView(PostView):
    template_name = 'blog/posts_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = self.queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        current_page = context.pop('page_obj', None)
        context['current_page'] = current_page
        return context


class ContentsListView(PostView):
    template_name = 'blog/posts_list.html'
    paginate_by = 10
