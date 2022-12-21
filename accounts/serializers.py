from rest_framework import serializers
from .models import CustomUser
from django.conf import settings


class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=settings.USER_ROLE_TYPE)

    class Meta:
        model = CustomUser
        fields = "__all__"  # ["username", "email", "role", "password"]  # "__all__"  #
        # read_only_fields = (
        # "username",
        # "phone",
        # "address",
        # "email",
        # "role",
        # "password",
        # "is_active",
        # "is_staff",
        # )

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data["email"],
            username=validated_data["username"],
            role=validated_data["role"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


# class GetCustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = "__all__"
