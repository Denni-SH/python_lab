# login - admin
# password - administrator

from django.contrib import admin
from .models import Author, Book, Category

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)