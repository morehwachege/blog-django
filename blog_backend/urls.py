from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('account.urls')),
    path('art/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
