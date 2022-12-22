from rest_framework.authtoken import views
from django.urls import path, include
from .views import UserView,UserAllView
from accounts.views import CustomAuthToken

urlpatterns = [
    path("api-token-auth/", CustomAuthToken.as_view()),
    path("users/", UserView.as_view()),
    path("users/all/", UserAllView.as_view()),
    # path("users/<str:pk>", UserView.as_view()),
]
