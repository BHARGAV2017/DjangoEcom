# from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CustomUserSerializer
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser


class IsAdminOrRole(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(request.user, type(request.user))
        # print(request.method)

        if request.method == "GET":
            print("inside get request")
            return True
        elif isinstance(request.user, AnonymousUser) and request.method == "POST":
            return True
        elif request.user.role == "A" or request.user.is_superuser:
            return True
        else:
            return False


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class UserView(APIView):
    """get/ delete a user"""

    permission_classes = [IsAdminOrRole]

    # Actually only admin can view all the users
    # Only owner can view his accounts details

    def get(self, request):
        """get all the details of a specific users"""
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def post(self, request):

        create_serializer = CustomUserSerializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)
        create_serializer.save()
        user = CustomUser.objects.get(username=create_serializer.data["username"])
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response(
            {"status": 200, "payload": create_serializer.data, "token": str(token_obj)}
        )

    # Only owner can delete his accounts
    def delete(self, request, *args, **kwargs):
        request.user.delete()
        response = Response()
        response.data = {"message": "User is deleted successfully"}
        return Response(response.data)

    """
    def post(self, request):
        all_dict = request.data
        CustomUser.objects.create(
            username=all_dict["username"],
            email=all_dict["email"],
            password=all_dict["password"],
            role=all_dict["role"],
        )
        return Response(data=all_dict)
    """

    """
    # part of get
        data = []
        user_data = CustomUser.objects.filter(
            username=request.data["username"]
        ).first()
        id = request.GET["id"]
        user = CustomUser.objects.filter(id=id).first()
        serializer = GetCustomUserSerializer(user)
        return Response(data=serializer.data)

        user = CustomUser.objects.filter(id=pk).first()
        print(user.email)
        print(user.id, type(user.id))

        user_data = user.objects.filter(id=user.id)
        serializer = GetCustomUserSerializer(user_data, many=True)
        print(user_data.id, type(user_data.id))

        users = CustomUser.objects.all()
        for user in users:
            temp = dict()
            temp["username"] = user.username
            data.append(temp)
        return Response(data=data)
    """

    # class UserCreate(APIView):
    """Create user"""

class UserAllView(APIView):
    def get(self, request):
        data= []
        all_users = CustomUser.objects.all()
        for user in all_users:
            # print(user.username)
            data.append([user.username, user.role])
        
        return Response(data=data)