from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique= True, )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.category_name)

class Item(models.Model):
    item_name = models.CharField(max_length=30)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price_per_item = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE )

    def __str__(self):
        return str(self.item_name)

