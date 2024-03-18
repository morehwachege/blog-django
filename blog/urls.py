from django.urls import path
from . import api

urlpatterns = [
    path('blogs/', api.get_blogs, name='get_blogs'),
    path('blogs/categories/', api.get_categories, name="get_categories"),
    path('blogs/<int:pk>/', api.get_blog, name='get_blog'),
    path('blogs/create/', api.create_blog, name='create_blog'),
    path('blogs/<int:pk>/update/', api.update_blog, name='update_blog'),
    path('blogs/<int:pk>/delete/', api.delete_blog, name='delete_blog'),
]

