from django.contrib import admin
from .models import *

class BookInfoAdmin(admin.ModelAdmin):
    model = BookInfo
    list_display = ['book_name', 'price', 'publish_date']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(BookSold)