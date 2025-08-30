from django.contrib import admin
from myportfolio.models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number',)
    list_filter = ('name', 'email')
    search_fields = ('name',)
