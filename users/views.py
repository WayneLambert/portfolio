from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from .models import Profile


class UserRegisterView(CreateView):
    model = Profile
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('blog:users:login')


class ProfileView(DetailView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['username'] = User.objects.get(username=kwargs['username'])
        return context

    def get(self, request, **kwargs):
        try:
            context = {
                'user': User.objects.get(username=kwargs['username']),
            }
        except User.DoesNotExist:
            context = None
            return TemplateResponse(request, template='errors/404.html')

        return render(request, self.template_name, context)


@login_required
def profile_update(request, **kwargs):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('blog:users:profile', kwargs['username'])
    else:
        try:
            if request.user.username == kwargs['username']:
                user_form = UserUpdateForm(instance=request.user)
                profile_form = ProfileUpdateForm(instance=request.user.user)
            else:
                raise PermissionDenied()
        except:
            return TemplateResponse(request, template='errors/403.html', status=403)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile_update.html', context)
