from django.contrib import admin
from django.db import models
from django.db.models import Count
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe

from apps.blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'slug', 'post_count', 'created_date', )
    prepopulated_fields = {'slug': ('name',)}

    def get_queryset(self, request):
        """ Calculation number of published posts by given category """
        queryset = super().get_queryset(request)
        queryset = queryset.filter(
            posts__status=1).annotate(_post_count=Count('posts', distinct=True))
        return queryset

    def post_count(self, obj):
        return obj._post_count


class PostAdmin(admin.ModelAdmin):
    fields = (
        'title', 'slug', 'content', 'reference_url', 'author',
        'categories', ('image', 'post_image'), 'status',
    )
    list_display = ('title', 'status', 'publish_date', 'updated_date')
    list_filter = ('status', 'categories', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'updated_date'
    readonly_fields = ['post_image', ]

    radio_fields = {
        'status': admin.HORIZONTAL,
    }

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.URLField: {'widget': TextInput(attrs={'size': '120'})},
    }

    def post_image(self, obj):
        img_width = obj.image.width * 0.25
        img_height = obj.image.height * 0.25
        return mark_safe(  # nosec
            f"<img src='{obj.image.url}' width='{img_width}' height='{img_height}' />")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
