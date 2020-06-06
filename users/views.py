from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Your account has been created! You are now able to log in')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('users:profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile_update.html', context)
