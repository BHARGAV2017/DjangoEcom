from rest_framework import serializers
from .models import Item

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id","seller_id","qty", "price_per_item"]

# class SellerItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SellerItem
#         fields = '__all__'
