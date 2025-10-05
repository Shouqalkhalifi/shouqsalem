from django.contrib import admin
from .models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "product_type", "weight", "created_at")
    list_filter = ("category", "product_type", "created_at")
    search_fields = ("name", "description")

    fieldsets = (
        ("معلومات المنتج", {
            "fields": ("name", "description", "price", "category", "product_type", "weight", "image")
        }),
        ("تفاصيل إضافية", {
            "fields": ("created_at",),
            "classes": ("collapse",),
        }),
    )
    readonly_fields = ("created_at",)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj and obj.product_type == "digital":
            fields = [f for f in fields if f != "weight"]  # إخفاء الوزن للمنتجات الرقمية
        return fields
