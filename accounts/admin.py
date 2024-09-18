from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("phone",)


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    list_display = (
        "phone",
        
        "is_superuser",
        "is_staff",
    )
    list_filter = (
        "phone",
        
        "is_superuser",
        "is_staff",
    )
    search_fields = ("phone",)
    ordering = ("phone",)
    fieldsets = (
        (
            "user",
            {
                "fields": ("phone", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": ("is_staff", "is_superuser"),
            },
        ),
        (
            "group_permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "important_date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            "Add User",
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    
                ),
            },
        ),
    )


# Register your models here.
admin.site.register(User, CustomUserAdmin)