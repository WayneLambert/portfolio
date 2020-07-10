from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('full_name', 'email', 'submit_date',)
    search_fields = ('first_name', 'last_name', 'email',)
    readonly_fields = ('submit_date',)
    ordering = ('first_name',)

admin.site.register(Contact, ContactAdmin)
