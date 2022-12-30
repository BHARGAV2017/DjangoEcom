from django.urls import include, path
from analytics.views import AnalyticsAPIView

# # from products.views import PersonViewSet, SpeciesViewSet

# # router = routers.DefaultRouter()
# # router.register(r'people', PersonViewSet)
# # router.register(r'species', SpeciesViewSet)


urlpatterns = [
    path('', AnalyticsAPIView.as_view()),
   
]

