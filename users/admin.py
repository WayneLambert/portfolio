from django.contrib import admin
from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'author_view',)


admin.site.register(Profile, ProfileAdmin)
