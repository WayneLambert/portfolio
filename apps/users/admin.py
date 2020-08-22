from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from apps.users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'author_view',)
    readonly_fields = ('profile_picture_image', )

    def profile_picture_image(self, obj):
        img_width = obj.profile_picture.width
        img_height = obj.profile_picture.height
        url = obj.profile_picture.url
        return mark_safe(  # nosec
            f"<img src='{url}' width='{img_width}' height='{img_height}' />")


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)
