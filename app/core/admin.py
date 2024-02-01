"""
Django Admin Customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _ # noqa

from core import models


class UserAdmin(BaseUserAdmin):
    """Admin for user model"""
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name",)}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser")}
        ),
        ("Important Dates", {"fields": ("last_login",)})
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "name",
                "is_staff",
                "is_superuser",
                "is_active")
        }),
    )


admin.site.register(models.User, UserAdmin)
