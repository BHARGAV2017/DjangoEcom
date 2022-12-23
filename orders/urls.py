from django.urls import include, path
from orders.views import OrderAPIView, ListAllOrders


urlpatterns = [
    path("order/", OrderAPIView.as_view()),
    path("orders/all/", ListAllOrders.as_view()),
]

"""path("order-items/", OrderItemView.as_view()),
path("order/", OrderView.as_view())

path('order/<str:pk>', OrderView.as_view()),
path('category/<str:pk>', CatItemView.as_view()),
path('category/', CatItemView.as_view())
"""
