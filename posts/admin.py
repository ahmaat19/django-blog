from django.contrib import admin
from .models import Category, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)