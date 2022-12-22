from django.db import models

# from django.contrib.auth.models import User
from accounts.models import CustomUser
from products.models import Item

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default= 2)
    ord_qty = models.IntegerField(default= 0)
    checkout= models.BooleanField(default=False)
    order_amount = models.IntegerField(default =0)

    def __str__(self):
        return str(self.id)


class OrdersItem(models.Model):
    user_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.TextField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.user_order)
