from time import perf_counter

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.html import format_html
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from apps.blog import search
from apps.blog.forms import PostForm
from apps.blog.models import Category, Post


class PostView(ListView):
    """
    Custom view sets default behaviour for all list views to subclass
    and inherit for their own implementation
    """

    queryset = Post.published.all()
    context_object_name = "posts"
    category_list = Category.objects.all().prefetch_related("posts")
    extra_context = {"categories_list": category_list}

    def get_context_data(self, **kwargs):
        """Facilitates pagination and post count summary"""
        context = super().get_context_data(**kwargs)
        context["current_page"] = context.pop("page_obj", None)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """Permits a logged in user to create a new post"""

    form_class = PostForm
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if self.object.status == 0:
            return reverse("blog:home")
        else:
            return self.object.get_absolute_url()


class HomeView(PostView):
    """Drives the list of posts returned on the blog's home page"""

    template_name = "blog/home.html"
    paginate_by = 6
    paginate_orphans = 3


class IndexListView(PostView):
    """Facilitates the short contents page"""

    template_name = "blog/index_page.html"


class ContentsListView(PostView):
    """Facilitates the contents page"""

    template_name = "blog/contents.html"
    paginate_by = 10
    paginate_orphans = 3

    def get_context_data(self, **kwargs):
        """Get's the author's name/username for presenting in the template"""
        context = super().get_context_data(**kwargs)
        context["author"] = Post.published.first().author
        return context


class AuthorPostListView(PostView):
    """Drives the list of posts written by a given author"""

    template_name = "blog/author_posts.html"
    paginate_by = 6
    paginate_orphans = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return super().get_queryset().filter(author=user)

    def get_context_data(self, **kwargs):
        """Get's the author's name/username for presenting in the template"""
        context = super().get_context_data(**kwargs)
        context["display_name"] = Post.published.first().author.profile.display_name
        return context


class CategoryPostListView(PostView):
    """Drives the list of posts for a given category."""

    template_name = "blog/category_posts.html"
    paginate_by = 6
    paginate_orphans = 3

    def get_queryset(self):
        self.categories = get_list_or_404(Category, slug=self.kwargs["slug"])
        return self.queryset.filter(categories=self.categories[0].id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = self.categories
        return context


class SearchView(TemplateView):
    """In minimalist style, à la Google, provides a search box"""

    template_name = "search.html"


class SearchResultsView(PostView):
    """Facilitates the search results"""

    template_name = "blog/search_results.html"
    paginate_by = 10
    paginate_orphans = 2
    relevancy_factor = 0.2

    def get_queryset(self):
        start_time = perf_counter()
        initial_query = format_html(self.request.GET.get("q"))
        if cleaned_query := search.cleanup_string(initial_query):
            search_vector = SearchVector("title", weight="A") + SearchVector("content", weight="B")
            search_query = SearchQuery(cleaned_query)
            search_rank = SearchRank(search_vector, search_query)
            qs = (
                Post.published.annotate(rank=search_rank)
                .filter(rank__gte=self.relevancy_factor)
                .order_by("-rank")
            )
            end_time = perf_counter()
            self.extra_context.update(
                {
                    "query": initial_query,
                    "cleaned_query": cleaned_query,
                    "time_taken": f"{end_time - start_time:.3f}",
                }
            )
            return qs
        else:
            msg = "A blank search cannot be submitted. Please enter a valid search query."
            messages.add_message(self.request, messages.INFO, msg)
            return self.queryset.none()

    def get_context_data(self, **kwargs):
        """Get's the author object for presenting in the template"""
        context = super().get_context_data(**kwargs)
        context["author"] = Post.published.first().author
        return context


class PostDetailView(DetailView):
    """Provides the individual post's page"""

    model = Post
    category_list = Category.objects.all().prefetch_related("posts")
    extra_context = {"categories_list": category_list}

    def get_context_data(self, **kwargs):
        """Facilitates detail page's pagination buttons"""
        context = super().get_context_data(**kwargs)
        context["author"] = Post.published.first().author
        context["profile"] = context["author"].profile
        posts = Post.published.all()
        posts_count = len(posts)

        for idx, post in enumerate(posts):
            if post.slug == self.kwargs["slug"]:
                context["prev_post"] = posts[posts_count - 1] if idx == 0 else posts[idx - 1]
                context["next_post"] = posts[0] if idx == posts_count - 1 else posts[idx + 1]
                return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Permits a logged in user to update an existing post they own"""

    model = Post
    form_class = PostForm
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool:
        post = self.get_object()
        return self.request.user.id == post.author.id


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Permits a logged in user to delete an existing post they own"""

    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("blog:home")

    def test_func(self) -> bool:
        post = self.get_object()
        return self.request.user.id == post.author.id
