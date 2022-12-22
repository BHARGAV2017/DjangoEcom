from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer, ItemUpdateSerializer
from accounts.models import CustomUser
from .models import Item
from rest_framework import status

#todo permission only for seller / admin

class ItemAPIView(APIView):
    def post(self, request):
        userobj = CustomUser.objects.get(email=request.user)
        data = request.data  #  we fill that according serializer reqirment ie{"seller": 2}
        data["seller"] = userobj.pk  # ie{"seller": 2}
        # print(request.data, user.pk) # request.data = {"user": 2}, user.pk= 2
        # print(type(request.data), type(user.pk)) # dict , int
    
        serializer = ItemSerializer(data=data)
        serializer.is_valid(raise_exception=True)  
        serializer.save()
        return Response({"data": serializer.data, "message": "Item is stored"})

    def get(self, request):
        serializer = ItemSerializer(Item.objects.all(), many=True)
        return Response(serializer.data)

    # def delete(self, request):
    #     # request.user.delete()
    #     # Response({"message": "Order deleted"})
    #     pass

    def delete(self, request):
        """Delete item by id """
        item_id= request.data.get('item_id')
        item = Item.objects.filter(id= item_id)
        item.delete()
        return Response({"status":status.HTTP_200_OK,"message": "Order deleted"})
        
    def put(self, request):
        id = request.data.get('id')
        qty = request.data.get('qty')
        price_per_item = request.data.get('price_per_item')
        seller_id = request.data.get('seller_id')
        serializer= ItemUpdateSerializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        try:
            update_obj = Item.objects.filter(id = id,seller_id = seller_id).first()
            update_obj.qty = qty
            update_obj.price_per_item = price_per_item
            # print(update_obj.qty)
            update_obj.save()
            # print(update_obj)
            return Response({"status":status.HTTP_200_OK,"message":"Item Updated"})
        except Exception as e:
            return Response({"message":str(e)})
