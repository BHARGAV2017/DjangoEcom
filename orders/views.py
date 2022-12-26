from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer,OrderUpdateSerializer
from accounts.models import CustomUser
from .models import Order, Item
from rest_framework import status
from rest_framework import permissions 


class OnlyAdminSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.is_superuser or request.user.role == "A":
                return True
        except Exception as e:
            print(e)

        return False

"""
# permission #
change is only reflected to that user account not for all accounts of Order table
and can perform CRUD for that account.

"""

class IsBuyersOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(request.user, type(request.user))
        # print(request.method)
        if request.user.role == "A" or request.user.is_superuser or request.user.role == "B":
            return True
        else:
            return False


class OrderAPIView(APIView):
    permission_classes = [IsBuyersOrAdmin]

    def post(self, request):
        userobj = CustomUser.objects.get(email=request.user)
        data = request.data.copy()  # request.data is blank but we fill that according serializer reqirment ie{"user": 3}
        data["user"] = userobj.pk  # ie{"user": 3}
        # print(request.data, user.pk) # request.data = {"user": 3}, user.pk= 3
        # print(type(request.data), type(user.pk)) # dict , int
        item = Item.objects.get(id=data["item"])
        ord_qty = data["ord_qty"]
        if (int(item.qty) - int(ord_qty))>= 0:
            item.qty = int(item.qty) - int(ord_qty)
            data["order_amount"] = int(ord_qty) * int(item.price_per_item)
            # data["item"] = item.pk
            serializer = OrderSerializer(data=data)
            serializer.is_valid(raise_exception=True) 
            serializer.save()
            item.save()
            return Response({"status":status.HTTP_200_OK,"message":"Order is sucessfully Updated"})
        else:
            return Response({"message": "Product is not available"})

    def get(self, request):
        # userobj = CustomUser.objects.get(email=request.user)
        serializer = OrderSerializer(Order.objects.filter(user_id= request.user.id), many=True)
        return Response(serializer.data)

    def delete(self, request):
        user_id= request.data.get('user_id')
        ord = Order.objects.filter(user_id=user_id).first() 
        ord.delete()
        return Response({"status":status.HTTP_200_OK,"message": "Order deleted"})

    def put(self, request):
        userobj = CustomUser.objects.get(email=request.user)
        # userobj.role
        # print(request.user)
        # print("pkkkkkkkkkkkkkkk",userobj.pk)
        id = request.data.get('id')
        user_id = userobj.pk ## Note user_id is not necessary it will extract from request.user
        ord_qty = request.data.get('ord_qty')
        item_id = request.data.get('item_id')
        # user_id = request.data.get('user_id') user_id is not needed
        serializer= OrderUpdateSerializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        try:
            update_obj = Order.objects.filter(id = id,user_id= user_id).first()
            # update_obj = Order.objects.filter(id = id).first()
            update_obj.ord_qty = ord_qty
            item = Item.objects.get(id=item_id)
            
            if (int(item.qty) - int(ord_qty))>= 0:
                item.qty = int(item.qty) - int(ord_qty)
                update_obj.order_amount = int(ord_qty) * int(item.price_per_item)
                update_obj.item = item
                update_obj.save()
                item.save()
                return Response({"status":status.HTTP_200_OK,"message":"Order is sucessfully Updated"})
            else:
                return Response({"message": "Product is not available"})
        except Exception as e:
            return Response({"message": str(e)})


class ListAllOrders(APIView):
    permission_classes = [OnlyAdminSuperuser]
    def get(self, request, *args, **kwargs):    
        serializer = OrderSerializer(Order.objects.all(), many=True)
        return Response(serializer.data)
