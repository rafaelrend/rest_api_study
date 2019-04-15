from django.contrib import admin
from .models import Book, Files, Item

# Register your models here.

admin.site.register(Book)
admin.site.register(Files)
# admin.site.register(Item)