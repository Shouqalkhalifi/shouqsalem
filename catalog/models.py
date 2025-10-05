from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField   # ✅ استدعاء CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    slug = models.SlugField(unique=True, verbose_name="المعرف")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    PRODUCT_TYPES = (
        ("digital", "منتج رقمي"),
        ("physical", "منتج ملموس"),
    )

    name = models.CharField(max_length=150, verbose_name="اسم المنتج")
    description = models.TextField(blank=True, verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="التصنيف"
    )

    product_type = models.CharField(
        max_length=10,
        choices=PRODUCT_TYPES,
        default="digital",
        verbose_name="نوع المنتج"
    )

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="وزن المنتج (كجم)"
    )

    # ✅ الحقل أصبح CloudinaryField بدلاً من ImageField
    image = CloudinaryField(
        "صورة المنتج",
        folder="products",     # كل الصور تخزن في فولدر اسمه products داخل حسابك Cloudinary
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:product_detail", args=[self.pk])
