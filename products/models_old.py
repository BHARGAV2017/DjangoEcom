# from django.db import models
# from accounts.models import CustomUser

# # Create your models here.


# class Category(models.Model):
#     category_name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return str(self.category_name)


# class Item(models.Model):
#     item_name = models.CharField(max_length=100)
#     model_no = models.CharField(max_length=100)
#     company_name = models.CharField(max_length=100)
#     category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
#     price_per_item = models.IntegerField(default=0)
#     seller_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.item_name)


# class SellerItem(models.Model):
#     seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)
#     per_qty_price = models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.item_id)
