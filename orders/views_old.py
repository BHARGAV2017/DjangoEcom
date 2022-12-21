# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Order, OrdersItem
# from accounts.models import *
# from .serializers import OrderSerializer, OrderItemSerializer
# from django.http import Http404
# from rest_framework import status


# class OrderView(APIView):
#     """Get a list of orders"""

#     def get(self, request, *args, **kwargs):
#         order_id = request.GET["id"]
#         obj = Order.objects.get(id=order_id)
#         print(obj.user.role)
#         res = {"role": str(obj.user.role)}
#         return Response(res)


# class OrderItemView(APIView):
#     def get(self, request, *args, **kwargs):
#         order_item_id = request.GET["id"]
#         obj = OrdersItem.objects.get(id=order_item_id)
#         print(obj.user_order.user.role)
#         res = {
#             "email": str(obj.user_order.user.email),
#             "role": str(obj.user_order.user.role),
#             "order_id": str(obj.user_order.id),
#             "order item name": str(obj.item.item_name),
#             "order item qty": str(obj.quantity),
#             "stock item qty": str(obj.seller_item.quantity),
#         }
#         return Response(res)

#     def post(self, request, format=None, *args, **kwargs):
#         email = request.data["email"]
#         data = request.data
#         print(data)
#         print(email)

#         user_data = CustomUser.objects.filter(email=email).first()
#         print("Role", type(user_data.role))

#         if user_data.role == "A" or user_data.role == "B":

#             serializer = OrderItemSerializer(data=data)
#             if not serializer.is_valid():
#                 return Response(
#                     {"message": "Invalid Order"}, status=status.HTTP_400_BAD_REQUEST
#                 )
#             serializer.save()
#             response = Response()
#             response.data = {
#                 "message": "Order is Created Successfully",
#                 "data": serializer.data,
#             }

#             return response

#         else:
#             response = Response()
#             response.data = {"message": "A seller cannot create order"}
#             return response
