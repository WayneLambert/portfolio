from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render, reverse
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from shapeshifter.views import MultiModelFormView

from apps.users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from apps.users.models import Profile


class UserRegisterView(CreateView):
    model = Profile
    form_class = UserRegisterForm
    template_name = 'users/register.html'
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

    def form_invalid(self, form):
        if self.user_exists():
            messages.error(self.request, message=self.USER_ALREADY_EXISTS_MSG)
            return redirect(reverse('blog:users:register'))

    def get_success_url(self):
        return reverse('blog:users:login')


class ProfileView(DetailView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['username'] = get_user_model().objects.get(username=kwargs['username'])
        return context

    def get(self, request, **kwargs):
        try:
            context = {
                'user': get_user_model().objects.get(username=kwargs['username']),
            }
        except get_user_model().DoesNotExist:
            context = None
            return TemplateResponse(request, template='errors/404.html')

        return render(request, self.template_name, context)


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, MultiModelFormView):
    """
    Any user attempting to GET the profile update page of another user,
    whether present in the DB or not, will receive a 403 error.
    """
    form_classes = (UserUpdateForm, ProfileUpdateForm)
    template_name = 'users/profile_update.html'

    def get_success_url(self):
        return reverse_lazy(
            'blog:users:profile', kwargs={'username': self.request.user.username})

    def test_func(self) -> bool:
        return self.request.user.username == self.kwargs['username']

    def get_instances(self) -> dict:
        return {
            'userupdateform': self.request.user,
            'profileupdateform': self.request.user.user
        }
