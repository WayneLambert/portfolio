from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, TemplateView

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


@login_required
def profile(request, **kwargs):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('blog:users:profile', kwargs['slug'])
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile_update.html', context)
