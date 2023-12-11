from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from two_factor.views import QRGeneratorView

from apps.users.views import (
    ProfileUpdateView,
    ProfileView,
    UserLoginView,
    UserPasswordResetCompleteView,
    UserPasswordResetConfirmView,
    UserPasswordResetDoneView,
    UserPasswordResetView,
    UserRegisterView,
    UserSetupEmailTokenView,
    UserSetupEmailView,
    UserSetupQRView,
)


app_name = "users"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("<slug:username>/profile/", ProfileView.as_view(), name="profile"),
    path("<slug:username>/profile/update/", ProfileUpdateView.as_view(), name="profile_update"),
]

# Custom Login, Two-Factor Authentication and Password Reset Processes
urlpatterns += [
    path("login/", UserLoginView.as_view(), name="login"),
    path("two-factor/setup/qr/", UserSetupQRView.as_view(), name="setup"),
    path("two-factor/qrcode/", QRGeneratorView.as_view(), name="qr"),
    path("two-factor/setup/email/", UserSetupEmailView.as_view(), name="setup_email"),
    path(
        "two-factor/setup/email/token/",
        UserSetupEmailTokenView.as_view(),
        name="setup_email_token",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password-reset/", UserPasswordResetView.as_view(), name="password_reset_form"),
    path("password-reset/done/", UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        UserPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
