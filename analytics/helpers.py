# TODO:: Raw Query using Q operator
# TODO:: top 3 frequent buyers and top 3 high paying buyers in each city

from products.models import Item
from orders.models import Order
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth, TruncYear,ExtractYear

# which user has the highest sell
def users_highest_sell():
    result =Order.objects.values("user_id__email").annotate(price_sum=Sum("order_amount") ).order_by("-price_sum")
    return result[:7]

# Which category of products sells most
def get_highest_sell_category():
    result = Order.objects.values("item_id__category_id__category_name").annotate(price_sum = Sum("order_amount")).order_by("-price_sum")
    return result[:7]

# Which perticular product sold most
def most_sell_products():
    result = Order.objects.values("item_id__item_name").annotate(price_sum = Sum("order_amount")).order_by("-price_sum")
    return result[:7]

# Find number of orders for each category of products
def most_ordered_products_by_category():
    result = Order.objects.values("item_id__item_name").annotate(price_sum = Count("item_id")).order_by("-price_sum")
    return result[:7]

# Find monthwise total sell for each year
def monthwise_total_sell():
    result = Order.objects.annotate(month= TruncMonth('order_date')).values('month').annotate(year= TruncYear('order_date')).annotate(ord_sum=Sum('order_amount')).order_by("-ord_sum")
    return result[:7]

# Highest number of orders by date
def sells_by_input_year(year):
    result = Order.objects.annotate(year= ExtractYear('order_date')).values('year').annotate(sum_ordamount = Sum('order_amount')).order_by('-sum_ordamount')
    return result.filter(year=year)

# Using raw query find monthwise total amount when given as input
def orders_by_month_raw(date):
    result= []
    print(date)
    for ord in Order.objects.raw(f"select id, strftime('%Y-%m', order_date) as d, sum(order_amount) as s from orders_order where d = '{date}' group by d order by  s desc"):
        result.append([ord.d, ord.s])

    return result



# print(users_highest_sell())
# print("****************************************")
# print(get_highest_sell_category())
# print("****************************************")
# print(most_sell_products())
# print("****************************************")
# print(most_ordered_products_by_category())
# print("****************************************")
# print(monthwise_total_sell())
# print("****************************************")
# print(sells_by_input_year('2019'))
# print("****************************************")
# print(monthwise_total_sell())
# print("****************************************")
# print(orders_by_month_raw('2021-11'))
# print("****************************************")







# Highest number of orders by date 
# city wise highest number of orders.
# How much customers orders products more than once within a month.
