from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from analytics.helpers import *
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authentication import 
# Create your views here.

class AnalyticsAPIView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        func  = str(self.request.query_params.get('func'))

        if 'highest_sell_by_customer' == func:
            return Response(status = status.HTTP_200_OK, data ={"data":users_highest_sell()})
        if 'highest_sell_by_category' == func:
            return Response(status = status.HTTP_200_OK, data ={"data":get_highest_sell_category()})
        if 'most_selling_product' == func:
            return Response(status = status.HTTP_200_OK, data ={"data":most_sell_products()})
        if 'most_ordered_items' == func:
            return Response(status = status.HTTP_200_OK, data ={"data":most_ordered_products_by_category()}) 
        if 'monthwise_sells' == func:
            return Response(status = status.HTTP_200_OK, data ={"data":monthwise_total_sell()}) 
        if 'sells_by_input_years' == func:
            year = str(self.request.query_params.get('year') )
            return Response(status = status.HTTP_200_OK, data ={"data":sells_by_input_year(year)}) 
        if 'sells_by_input_months' == func:
            YearMonth = str(self.request.query_params.get('year-month'))
            return Response(status = status.HTTP_200_OK, data ={"data":orders_by_month_raw(YearMonth)}) 
        return Response(status = status.HTTP_200_OK, data = {"message": "Invalid"})
