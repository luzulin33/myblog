from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'modified_time', 'tag']

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)

admin.site.register(Post, PostAdmin)