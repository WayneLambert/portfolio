from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from apps.users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'author_view', 'created_date', 'updated_date')
    readonly_fields = ('profile_picture_image', 'created_date', 'updated_date')

    def profile_picture_image(self, obj):
        try:
            img_width = obj.profile_picture.width * 0.5
            img_height = obj.profile_picture.height * 0.5
            url = obj.profile_picture.url
            return format_html(
                f"<img src='{url}' width='{img_width}' height='{img_height}' />")
        except OSError:
            pass


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)
