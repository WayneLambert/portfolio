from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.blog.forms import PostForm
from apps.blog.models import Category, Post


class PostView(ListView):
    """
    Custom view sets default behaviour for all list views to subclass
    and inherit for their own implementation
    """
    model = Post
    context_object_name = 'posts'
    category_list = Category.objects.all().prefetch_related('posts')
    extra_context = {'categories_list': category_list}
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')
    queryset = queryset.filter(status=1)

    def get_context_data(self, **kwargs):
        """ Facilitates pagination and post count summary """
        context = super(PostView, self).get_context_data(**kwargs)
        context['current_page'] = context.pop('page_obj', None)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """ Permits a logged in user to create a new post """
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """ Return the URL to redirect to after processing a valid form. """
        if self.object.status == 0:
            return reverse('blog:home')
        else:
            return self.object.get_absolute_url()


class HomeView(PostView):
    """ Drives the list of posts returned on the blog's home page """
    template_name = 'blog/home.html'
    paginate_by = 6
    paginate_orphans = 3

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['num_posts'] = self.queryset.count
        return context

class IndexListView(PostView):
    """ Facilitates the short contents page """
    template_name = 'blog/index_page.html'


class ContentsListView(PostView):
    """ Facilitates the contents page """
    template_name = 'blog/contents.html'
    paginate_by = 20
    paginate_orphans = 3


class AuthorPostListView(PostView):
    """ Drives the list of posts written by a given author """
    template_name = 'blog/user_posts.html'
    paginate_by = 6
    paginate_orphans = 3

    def get_queryset(self):
        user = get_object_or_404(get_user_model(), username=self.kwargs['username'])
        return super(AuthorPostListView, self).get_queryset().filter(author=user)

    def get_context_data(self, **kwargs):
        """ Get's the author's name/username for presenting in the template """
        context = super(AuthorPostListView, self).get_context_data(**kwargs)
        qs = self.get_queryset()
        context['num_posts'] = qs.count
        if qs:
            context['display_name'] = qs.first().author.user.display_name  # pragma: no cover
        return context


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
        qs = self.get_queryset()
        context['num_posts'] = qs.count()
        return context


class SearchResultsView(PostView):
    """ Facilitates the search results """
    template_name = 'blog/search_results.html'
    paginate_by = 10
    paginate_orphans = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query))
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['query'] = context['view'].request.GET['q']
        context['num_posts'] = self.queryset.count()
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
        posts.filter(status=1)
        posts_count = len(posts)

        for idx, post in enumerate(posts):
            if post.slug == self.kwargs['slug']:
                context['prev_post'] = posts[posts_count - 1] if idx == 0 else posts[idx - 1]
                context['next_post'] = posts[0] if idx == posts_count - 1 else posts[idx + 1]
                return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Permits a logged in user to update an existing post """
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool:
        post = self.get_object()
        return self.request.user.id == post.author.id


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Permits a logged in user to delete an existing post """
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/blog/'

    def test_func(self) -> bool:
        post = self.get_object()
        return self.request.user.id == post.author.id
