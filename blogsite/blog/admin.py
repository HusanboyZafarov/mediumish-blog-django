from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'author']
    prepopulated_fields = {"slug": ('title',)}


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['name', 'email']
