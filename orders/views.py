from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from accounts.models import CustomUser
from .models import Order
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
        