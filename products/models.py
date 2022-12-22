from django.db import models
from accounts.models import CustomUser



class Item(models.Model):
    item_name = models.CharField(max_length=30)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price_per_item = models.IntegerField()

    def __str__(self):
        return str(self.item_name)