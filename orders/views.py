from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from accounts.models import CustomUser


class OrderAPIView(APIView):
    def post(self, request):
        print(request.user)
        # print(type(request.user))
        user = CustomUser.objects.get(email=request.user)
        print(user)
        print(user.role)
        serializer = OrderSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        # serializer.save()

        return Response({"payload": serializer.data, "message": "Order placed"})
