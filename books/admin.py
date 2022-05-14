from django.contrib import admin
from books.models import *

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)