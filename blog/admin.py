from django.contrib import admin
from .models import Blog, Category

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_categories', 'created_by', 'created_at', 'updated_at']
    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    display_categories.short_description = 'Categories'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    