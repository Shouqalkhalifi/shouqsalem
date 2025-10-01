from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

@admin.register(Account)
class AccountAdmin(UserAdmin):
    # الحقول التي تظهر في القائمة
    list_display = ("username", "email", "full_name", "phone", "is_staff", "is_active")
    search_fields = ("username", "email", "full_name", "phone")
    list_filter = ("is_staff", "is_active", "date_joined")

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("full_name", "phone")}),
    )
