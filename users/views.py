from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from .models import Profile


class UserRegisterView(CreateView):
    model = Profile
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('blog:users:login')


class ProfileView(TemplateView):
    template_name = 'users/profile.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_update.html'
    form_class = UserUpdateForm
    profile_form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        obj = super(ProfileUpdateView, self).get_object(queryset)
        if not self.request.user == obj.user:
            raise PermissionDenied()
        return obj

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        if 'user_form' not in context:
            context['user_form'] = self.form_class(instance=self.request.user)
        if 'profile_form' not in context:
            context['profile_form'] = self.profile_form_class(
                self.request.FILES, instance=self.request.user.user)
        return context

    def form_valid(self, form):
        user_form = UserUpdateForm(self.request.POST, instance=self.request.user)
        profile_form = ProfileUpdateForm(
            self.request.POST, self.request.FILES, instance=self.request.user)
        super(ProfileUpdateView, self).form_valid(form)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return super().form_valid(profile_form)

    def get_success_url(self):
        return reverse('blog:users:profile', kwargs={'slug': self.request.user.user.slug})
