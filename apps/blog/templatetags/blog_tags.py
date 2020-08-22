from django import template

from apps.blog.models import Category


register = template.Library()


@register.inclusion_tag('blog/sidebar.html')
def category_sidebar():
    blog_categories = Category.objects.all().order_by('name')
    return {'blog_categories': blog_categories}
