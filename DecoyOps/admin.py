from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    """Admin configuration for the Contact model.

    This class customizes the appearance and behavior of the Contact model in the Django admin panel.

    Attributes:
        list_display (tuple): A tuple of field names to display in the list view of the admin panel.
    """
    list_display = ('name', 'surname', 'email', 'message')

admin.site.register(Contact, ContactAdmin)

