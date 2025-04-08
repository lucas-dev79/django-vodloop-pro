from django.contrib import admin
from core.models import Podcast, Contact, Category
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    class Meta:
     model = Contact
     fields = ["name"]

admin.site.register(Podcast)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)