from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import Permission, IsAuthenticatedOrReadOnly
from analyticsApi.helpers import *
# from rest_framework.authentication import 
# Create your views here.

class AnalyticsAPIView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        return users_highest_sell()
