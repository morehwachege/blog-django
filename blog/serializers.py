from rest_framework import serializers
from .models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return obj.created_by.name if obj.created_by else None

    def get_categories(self, obj):
        return [{'id': category.id, 'name': category.name} for category in obj.categories.all()]

    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'created_at', 'updated_at', 'created_by', 'categories']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']