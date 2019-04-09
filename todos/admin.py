from django.contrib import admin
from .models import Todo, Project, Owner

admin.site.register(Todo)
admin.site.register(Project)
admin.site.register(Owner)
