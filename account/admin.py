from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.site_header = "Blog Administration"
admin.site.site_title = "Blog admin"
admin.site.index_title = "Welcome to Blog Admin Center"

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id','email', 'name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'avatar')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ['email', 'name']
    ordering = ['email']

admin.site.register(User, CustomUserAdmin)
