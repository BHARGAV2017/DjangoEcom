from rest_framework import serializers
from .models import Order, OrdersItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["item", "ord_qty"]

# # fields = ['user_order','item','quantity','seller_item']

# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrdersItem
#         fields = "__all__"
