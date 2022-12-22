from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer,OrderUpdateSerializer
from accounts.models import CustomUser
from .models import Order, Item
from rest_framework import status

class OrderAPIView(APIView):
    def post(self, request):
        userobj = CustomUser.objects.get(email=request.user)
        data = request.data  # request.data is blank but we fill that according serializer reqirment ie{"user": 3}
        data["user"] = userobj.pk  # ie{"user": 3}
        # print(request.data, user.pk) # request.data = {"user": 3}, user.pk= 3
        # print(type(request.data), type(user.pk)) # dict , int

        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)  #
        serializer.save()

        return Response({"data": serializer.data, "message": "Order placed"})

    def get(self, request):
        serializer = OrderSerializer(Order.objects.all(), many=True)
        return Response(serializer.data)

    def delete(self, request):
        user_id= request.data.get('user_id')
        ord = Order.objects.filter(user_id=user_id).first() 
        ord.delete()
        return Response({"status":status.HTTP_200_OK,"message": "Order deleted"})

    def put(self, request):
        userobj = CustomUser.objects.get(email=request.user)
        userobj.role
        # print(userobj.pk)
        id = request.data.get('id')
        # id = userobj.pk
        ord_qty = request.data.get('ord_qty')
        item_id = request.data.get('item_id')
        user_id = request.data.get('user_id')
        serializer= OrderUpdateSerializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        try:
            # update_obj = Order.objects.filter(id = id,user_id= user_id).first()
            update_obj = Order.objects.filter(id = id).first()
            update_obj.ord_qty = ord_qty
            item = Item.objects.get(id=item_id)
            item.qty = int(item.qty) - int(ord_qty)
            update_obj.order_amount = int(ord_qty) * int(item.price_per_item)
            update_obj.item = item
            update_obj.save()
            item.save()
            return Response({"status":status.HTTP_200_OK,"message":"Order is sucessfully Updated"})
        except Exception as e:
            return Response({"message": str(e)})
