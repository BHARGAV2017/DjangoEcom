from rest_framework import serializers
from .models import Order, OrdersItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


# # fields = ['user_order','item','quantity','seller_item']

# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrdersItem
#         fields = "__all__"
