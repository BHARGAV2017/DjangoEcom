# from django.shortcuts import render
# from rest_framework.views import APIView
# from products.models_old import Item, Category
# from rest_framework.response import Response
# from django.http import Http404
# from .serializers import ItemSerializer

# # Create your views here.
# # creating lists of all items


# class ItemView(APIView):
#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated, IsAdminUser)

#     def get_object(self, pk):
#         try:
#             return Item.objects.get(pk=pk)
#         except Item.DoesNotExist:
#             raise Http404

#     def get(self, request, pk=None, format=None):
#         if pk:
#             items = self.get_object(pk)
#             serializer = ItemSerializer(items)
#         else:
#             items = Item.objects.all()
#             serializer = ItemSerializer(items, many=True)

#         return Response(serializer.data)

#         # items = Item.objects.all()
#         # for item in items:
#         #     temp = dict()
#         #     temp["item_name"] = item.item_name
#         #     data.append(temp)

#         # return Response(data=data)


# class CatItemView(APIView):
#     def get(self, request, pk=None, format=None):
#         if pk:
#             category_name = Category.objects.filter(pk=pk).first()
#             print(category_name)
#             cat_items = Item.objects.filter(category_name=category_name)
#             serializer = ItemSerializer(cat_items, many=True)
#         else:
#             cat_items = Item.objects.all()
#             serializer = ItemSerializer(cat_items, many=True)

#         return Response(serializer.data)
