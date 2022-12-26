from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer, ItemUpdateSerializer, CategorySerializer
from accounts.models import CustomUser
from .models import Item, Category
from rest_framework import status
from rest_framework import permissions

#todo permission only for seller / admin

class IsSellerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(request.user, type(request.user))
        # print(request.method)
        if request.user.role == "A" or request.user.is_superuser or request.user.role == "S":
            return True
        else:
            return False

class ItemAPIView(APIView):
    permission_classes =[IsSellerOrAdmin]

    def post(self, request):
        userobj = CustomUser.objects.get(email=request.user)
        data = request.data.copy()  #  we fill that according serializer reqirment ie{"seller": 2}
        print(data)
        # data["seller"]= request.data.get("seller")
        data["seller"] = userobj.pk  # ie{"seller": 2}
        # print(request.data, user.pk) # request.data = {"user": 2}, user.pk= 2
        # print(type(request.data), type(user.pk)) # dict , int
        data["item_name"] = request.data.get("item_name")
        item = Item.objects.filter(seller=data["seller"], item_name= data["item_name"]).first()
        if item:
            print("item_name", item.item_name)
            print("item_seller", item.seller)
            item.qty = item.qty + int(data["qty"])
            item.price_per_item = int(data["price_per_item"])
            item.save()
            return Response({"message": "Item is updated successfully"})
        else:
            serializer = ItemSerializer(data=data)
            serializer.is_valid(raise_exception=True)  
            serializer.save()
            return Response({"data": serializer.data, "message": "Item is stored"})
        # try:
        #     if item.item_name != data["item_name"]:
        #     else:
        # except Exception as e:
        #     print(e)
        #     return Response({"message":str(e)})


    def get(self, request):
        serializer = ItemSerializer(Item.objects.all(), many=True)
        return Response(serializer.data)

    # def delete(self, request):
    #     # request.user.delete()
    #     # Response({"message": "Order deleted"})
    #     pass

    def delete(self, request):
        """Delete item by id """
        item_id= request.data.get('item_id')
        item = Item.objects.filter(id= item_id)
        item.delete()
        return Response({"status":status.HTTP_200_OK,"message": "Order deleted"})
        
    def put(self, request):
        id = request.data.get('id')
        qty = request.data.get('qty')
        price_per_item = request.data.get('price_per_item')
        seller_id = request.data.get('seller_id')
        serializer= ItemUpdateSerializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        try:
            update_obj = Item.objects.filter(id = id,seller_id = seller_id).first()
            update_obj.qty = qty
            update_obj.price_per_item = price_per_item
            update_obj.save()
            return Response({"status":status.HTTP_200_OK,"message":"Item Updated"})
        except Exception as e:
            return Response({"message":str(e)})



class CategoryAPIView(APIView):
    def post(self, request):
        request.data["category_name"]=request.data.get("category_name").lower()
        serializer=CategorySerializer(data =request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
        
    def get(self):
        serializer = CategorySerializer(Category.objects.all(), many = True)
        return Response(serializer.data)

    def delete(self, request):
        cat = Category.objects.all()
        cat.delete()
        return Response({"status":status.HTTP_200_OK,"message": "Category deleted"})

# class ListAllItems(APIView):
#     permission_classes = [OnlyAdminSuperuser]
#     def get(self, request, *args, **kwargs):    
#         serializer = ItemSerializer(Item.objects.all(), many=True)
#         return Response(serializer.data)