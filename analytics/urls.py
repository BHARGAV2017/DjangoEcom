from django.urls import include, path
from analytics.views import AnalyticsAPIView
# from analytics.views import AnalyticsAPIView

urlpatterns = [
    path('', AnalyticsAPIView.as_view()),
    # path('category/', CategoryAPIView.as_view())
   
]