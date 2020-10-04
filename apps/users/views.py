from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from shapeshifter.views import MultiModelFormView

from apps.users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from apps.users.models import Profile


class UserRegisterView(CreateView):
    model = Profile
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:home')
    USER_ALREADY_EXISTS_MSG = """
        The username you've attempted to register with is already taken.
        Perhaps you already have an account? If so, you can log in using
        the link below, or register using a alternative username.
    """

    def user_exists(self) -> bool:
        username = self.request.POST['username']
        user = get_user_model().objects.filter(username=username)
        if user.exists():
            return True

    def form_valid(self, form):
        self.object = form.save()
        form_valid =  super().form_valid(form)
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user=user, backend=backend)
        return form_valid

    def form_invalid(self, form):
        if self.user_exists():
            messages.error(self.request, message=self.USER_ALREADY_EXISTS_MSG)
            return redirect(reverse('blog:users:register'))


class ProfileView(DetailView):
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), username=self.kwargs['username'])


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, MultiModelFormView):
    """
    Any user attempting to GET the profile update page of another user,
    whether present in the DB or not, will receive a 403 error.
    """
    form_classes = (UserUpdateForm, ProfileUpdateForm)
    template_name = 'users/profile_update.html'

    def test_func(self) -> bool:
        return self.request.user.username == self.kwargs['username']

    def get_instances(self) -> dict:
        return {
            'userupdateform': self.request.user,
            'profileupdateform': self.request.user.user
        }

    def get_success_url(self):
        return reverse_lazy(
            'blog:users:profile', kwargs={'username': self.request.user.username})
