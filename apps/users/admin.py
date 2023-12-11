import contextlib

from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from django_otp.plugins.otp_static.models import StaticDevice

from apps.users.models import EmailToken, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "author_view", "created_date", "updated_date")
    readonly_fields = ("profile_picture_image", "created_date", "updated_date")
    SCALE_FACTOR = 0.3

    def profile_picture_image(self, obj):
        with contextlib.suppress(OSError):
            img_width = obj.profile_picture.width * self.SCALE_FACTOR
            img_height = obj.profile_picture.height * self.SCALE_FACTOR
            url = obj.profile_picture.url
            return format_html(f"<img src='{url}' width='{img_width}' height='{img_height}' />")


class EmailTokenAdmin(admin.ModelAdmin):
    list_display = (
        "challenge_email_address",
        "challenge_generation_timestamp",
        "challenge_expiration_timestamp",
        "challenge_completed",
        "token_expiration_timestamp",
        "user_id",
    )
    exclude = ("challenge_token",)

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in obj._meta.fields if field.name != "challenge_token"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(EmailToken, EmailTokenAdmin)
admin.site.unregister(Group)
admin.site.unregister(StaticDevice)
