from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

from two_factor.views.mixins import OTPRequiredMixin


class DeviceAuthUserMixin(OTPRequiredMixin, LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self) -> bool:
        return self.request.user.profile.is_two_factor_auth_by_token

    def handle_no_permission(self):
        return redirect(settings.LOGIN_URL)


class EmailAuthUserMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self) -> bool:
        return self.request.user.profile.is_two_factor_auth_by_email

    def handle_no_permission(self):
        return redirect(settings.LOGIN_URL)


class TwoFactorAuthUserMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self) -> bool:
        return self.request.user.profile.is_two_factor_authenticated

    def handle_no_permission(self):
        html_msg = (
            "You have not verified by either device token or email.<br /><br />" +
            "Please follow the two-factor authentication process."
        )
        messages.add_message(self.request, messages.INFO, mark_safe(html_msg))
        return redirect(settings.LOGIN_URL)
