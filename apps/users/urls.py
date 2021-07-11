from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from two_factor.views import QRGeneratorView

from apps.users.views import (ProfileUpdateView, ProfileView, UserLoginView,
                              UserRegisterView, UserSetupView,)


app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<slug:username>/profile/', ProfileView.as_view(), name='profile'),
    path('<slug:username>/profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
]

# Custom Login and Password Reset Process
urlpatterns += [
    path('login/', UserLoginView.as_view(), name='login'),
    path('two-factor/setup/', UserSetupView.as_view(), name='setup'),
    path('two-factor/qrcode/', QRGeneratorView.as_view(), name='qr'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset_form.html',
             email_template_name='users/password_reset_email.html',
             subject_template_name='users/password_reset_subject.txt',
             success_url=reverse_lazy('blog:users:password_reset_done')),
         name='password_reset_form'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             success_url=reverse_lazy('blog:users:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
