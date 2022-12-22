from django.urls import include, path
from products.views import ItemAPIView

# # from products.views import PersonViewSet, SpeciesViewSet

# # router = routers.DefaultRouter()
# # router.register(r'people', PersonViewSet)
# # router.register(r'species', SpeciesViewSet)


urlpatterns = [
    path('items/', ItemAPIView.as_view()),
    # path('items/<str:pk>', ItemView.as_view()),
    # path('category/<str:pk>', CatItemView.as_view()),
    # path('category/', CatItemView.as_view())
]

