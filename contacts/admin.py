from django.contrib import admin
from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('full_name', 'email', 'submit_date',)
    search_fields = ('first_name', 'last_name', 'email',)

    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    full_name.admin_order_field = 'first_name'
    full_name.short_description = 'Full Name'


admin.site.register(Contact, ContactAdmin)
