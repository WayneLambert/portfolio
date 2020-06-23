from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Category, Post


class PostView(ListView):
    """ Custom view sets default behaviour for all list views to subclass
        and inherit for their own implementation """
    model = Post
    context_object_name = 'posts'
    category_list = Category.objects.all().prefetch_related('posts')
    extra_context = {'categories_list': category_list}
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        current_page = context.pop('page_obj', None)
        context['current_page'] = current_page
        context['num_posts'] = current_page.paginator.object_list.count()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """ Permits a logged in user to create a new post """
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class HomeView(PostView):
    """ Drives the list of posts returned on the blog's home page """
    template_name = 'blog/home.html'
    paginate_by = 6
    paginate_orphans = 3


class IndexListView(ListView):
    """ Facilitates the short contents page """
    model = Post
    template_name = 'blog/index_page.html'
    context_object_name = 'posts'
    category_list = Category.objects.all().prefetch_related('posts')
    extra_context = {'categories_list': category_list}
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')


class ContentsListView(PostView):
    """ Facilitates the contents page """
    template_name = 'blog/contents.html'
    paginate_by = 20
    paginate_orphans = 3


class UserPostListView(PostView):
    """ Drives the list of posts written by a given author """
    template_name = 'blog/user_posts.html'
    paginate_by = 6
    paginate_orphans = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return self.queryset.filter(author=user, status=1)


class CategoryPostListView(PostView):
    """ Drives the list of posts for a given category. """
    template_name = 'blog/category_posts.html'
    paginate_by = 6
    paginate_orphans = 3

    def get_queryset(self):
        self.categories = get_list_or_404(Category, slug=self.kwargs['slug'])
        return self.queryset.filter(categories=self.categories[0].id)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        return context


class SearchResultsView(PostView):
    """ Facilitates the search results """
    template_name = 'blog/search_results.html'
    paginate_by = 10
    paginate_orphans = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            qs = self.queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query))
        else:
            qs = self.queryset
        return qs

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['query'] = context['view'].request.GET['q']
        return context


class PostDetailView(DetailView):
    """ Provides the individual post's page """
    model = Post
    category_list = Category.objects.all().prefetch_related('posts')
    extra_context = {'categories_list': category_list}

    def get_context_data(self, **kwargs):
        """ Facilitates detail page's pagination buttons """
        context = super(PostDetailView, self).get_context_data(**kwargs)
        posts = Post.objects.prefetch_related('categories').select_related('author__user')
        for idx, post in enumerate(posts):
            if post.slug == self.kwargs['slug']:
                context['prev_post'] = posts[posts.count() - 1] if idx == 0 else posts[idx - 1]
                context['next_post'] = posts[0] if idx == posts.count() - 1 else posts[idx + 1]
                return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Permits a logged in user to update an existing post """
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user.id == post.author.id


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Permits a logged in user to delete an existing post """
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
