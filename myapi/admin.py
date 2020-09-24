from django.contrib import admin
from .models import Contacts

# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display   = ('first_name','address','phone')
    list_filter    = ('first_name','address')
    search_fields  = ('first_name','address')