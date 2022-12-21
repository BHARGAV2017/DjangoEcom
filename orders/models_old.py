# from django.db import models

# # from django.contrib.auth.models import User
# from accounts.models import CustomUser
# from products.models_old import *

# # Create your models here.
# class Order(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     payment_status = models.BooleanField()
#     total_price = models.IntegerField()
#     is_palced = models.BooleanField()

#     def __str__(self):
#         return str(self.id)


# class OrdersItem(models.Model):
#     user_order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     seller_item = models.ForeignKey(SellerItem, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.user_order)


# # class BuyerOrder(models.Model):
# #     user= models.
