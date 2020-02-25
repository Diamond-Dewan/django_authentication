from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'join_date', 'last_login', 'is_staff', 'is_admin')
    list_filter = ('is_staff', 'is_admin')

    # Field set display in admin form
    fieldsets = (
        ('User Info', {'fields': ('email', 'first_name', 'last_name', 'password',)}),
        ('Login info', {'fields': ('join_date', 'last_login')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    )

    # Field sets / Forms to add new User account
    add_fieldsets = (('Sign Up Form', {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),)

    ordering = ('email',)
    search_fields = ('email', 'is_admin',)
    readonly_fields = ('join_date', 'last_login')
    filter_horizontal = ()


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
