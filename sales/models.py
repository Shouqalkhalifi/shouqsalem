from django.db import models
from catalog.models import Product
from identity.models import Account


class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="orders", verbose_name="الحساب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    is_paid = models.BooleanField(default=False, verbose_name="مدفوع")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id} - {self.account.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"


class Favorite(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="favorites", verbose_name="الحساب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorited_by", verbose_name="المنتج")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("account", "product")
        verbose_name = "مفضلة"
        verbose_name_plural = "المفضلات"

    def __str__(self):
        return f"{self.account.username} ❤ {self.product.name}"
