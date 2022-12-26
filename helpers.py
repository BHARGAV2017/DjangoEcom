# calculate all business logic
# create items for each sellers
import requests
import random
import time
from random import randrange
from datetime import timedelta
from datetime import datetime

electronics = [
	("smartwatch",3000),
	("headphones",1500),
	("pendrive",1000),
	("memory card",800),
	("cameras",15000),
	("printer",6000),
	("tv",5000),
	]
	
mobile_phones = [
	("samsung",18000),
	("apple", 70000),
	("huawei",12000),
	("nokia",10000),
	("sony",22000),
	("lg",8000),
	("htc",5000),
	("motorola",16000),
	]
	
clothes = [
	("t shirt",400),
	("shirt",600),
	("sweater",700),
	("inner",300),
	("top",500),
	("jeans",1200),
	("trouser",900),
	("boxer",400),
	("track pants",700),
	("skirts",800),
	]

# for i in electronics:
#     print(i)
#     header = ""
#     data =
#     requests.post()



shoes= [
	("nike",8000),
	("adidas",7000),
	("puma",9000),
	("fila",6500),
	("bata",6000),
	("woodland",10000),
	("reebok",8000),
	]
	
personal_care=[
	("soap",40),
	("hand wash",50),
	("face wash",300),
	("body moisturizer",250),
	("shampoo",200),
	("conditioner",150),
	("toothpaste",50),
	("toothbrush",35),
	("face cream",150),
	]
book=[
	("physics",1500),
	("chemistry",1000),
	("maths",800),
	("biology",1200),
	("polity",700),
	("education",800),
	("history",800),
	("grography",1100),
	("novel",500),
	("poetry",400),
	("computer",1500),
	]

user_token = [ 
	("052b584426ed1097bf25b55b0b6edcd2bb912b9f",	2),
	("592454617afb00d1d5a291d5b52a3e6929546c11",	3),
	("e35de4929bbfae793d2943dfd2a0f5fc47c04714",	5),
	("ddfdd705c2a493bd2b6e049ffd8fc36b723de402",	6),
	("19fef3e43ee10ae3702207663afe77e1ca71c598",	7),
	("052be0c45d8d93bcf52aac222f9f91701f4416bf",	8),
	("c35728dbf0e9a422805bdc8f21ce61a1c1e94982",	9),
	("740f1a7e2723ecdc9c3c224ef02f4088898a53ac",	10),
	("d16047ddc5d9ad76af23f8bd3859084390360fa0",	11),
	("d43f8bb28cd64529e5817cdb94420d72fe303006",	12),
	("095b5ecf4469e8befc0c7df20980f5c6012eab53",	13),
	("97ff69a62d7a30853b2a0827300b6374ee357090",	14),
	("9260c56ff31d694379880052183e89357bea63cc",	15),
	("95e089c470d8c86265ee0407cb6eba95705b10be",	16),
	("ed9a25c303e0d10245296a49994e3708c8bf0d66",	17),
	("8e334095826485ba288295a86b393960732c57d0",	18),
	("998ef0797ff08b2122cf9047dfecc7332e5fbd1c",	19),
	("c67e6f8f0936f0904dae7f4c512f587b097ee826",	20),
	("5a8d161eafa408002fa08b5c3b3eaf36d547bee9",	21),
	("fce818274ebf2ac56b2b7e88b1e118af125687cb",	22),
	("0e8c997e2243d382c052d76d20c3813d50497285",	23),
	("2130914e90139e915184d49fffab81a0b01ae5ba",	24),
	("e0e0504a287a4d1098d78ccc8c10e54ec7ba32f5",	25),
	("3e71e3c319f44dffe181448c1f7204b457aa902d",	26),
	("a608828f3de0aea1df655c99ce825f00a20348d1",	27),

		]

buyers_tokens_id = [
	3,
	5,
	7,
	16,
	17,
	18,
	19,
	21,
	22,
	23,
	24,
	25,
	26,
	27,
]

sellers_tokens_id = [
	2,
	6,
	8,
	12,
	13,
	14,
	15,
	20,
	]


buyers_token= [i[0] for i in user_token if i[1] in buyers_tokens_id]
# print("Buyesr list",buyers_token)

seller_token = [i[0] for i in user_token if i[1] in sellers_tokens_id]
# print("Seller list",seller_token)

dict_mp= dict([
	(6,	electronics),
	(7,	mobile_phones),
	(8,	clothes),
	(9,	shoes),
	(10, personal_care),
	(11, book)
	])

# print("dict_mp",dict_mp)
# first create item table 
def create_item_table(n=100):
	for i in range(n):
		key_list= list(dict_mp.keys())
		random_category =random.choices(key_list)
		random_item = random.choices(dict_mp[random_category[0]])
		random_seller = random.choice(seller_token)
		item_name, price_per_item= random_item[0]
		qty = 10
		headers = {"Authorization":"token "+ random_seller}
		data = {
			"item_name":item_name,
			"qty":qty,
			"price_per_item":price_per_item,
			"seller":"",
			"category":random_category[0],
				}

		time.sleep(1)
		url = 'http://127.0.0.1:8000/api/products/items/'
		print("url>>>",url)
		print("headers>>>",headers)
		print("data>>>",data)
		r = requests.post(url= url, data= data, headers=headers)
		# print("random seller", random_seller)
		# print("ffffff>>>",random_category[0],random_item[0], random_seller)

#**************************************************************************************************************************

#create order

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 )
    random_second = randrange(int_delta)
    return (start + timedelta(minutes=random_second)).date()

def random_date_gen(start='1/1/2019', end= '1/1/2022'):
	d1 = datetime.strptime(start, '%m/%d/%Y')
	d2 = datetime.strptime(end, '%m/%d/%Y')
	# print(random_date(d1, d2))
	return random_date(d1, d2)

def create_order_table(n):
	for i in range(n):
		random_buyer = random.choice(buyers_token)
		item = random.randrange(175,333)
		ord_qty = random.randint(1,6)
		order_date = random_date_gen()
		headers = {"Authorization":"token "+ random_buyer}
		data = {
			"item":item,
			"ord_qty":ord_qty,
			"order_date":order_date,
				}

		# time.sleep(1)
		url = 'http://127.0.0.1:8000/api/orders/order/'
		print("url>>>",url)
		print("headers>>>",headers)
		print("data>>>",data)
		r = requests.post(url= url, data= data, headers=headers)
		if r.status_code != 200:
			print(r.text)
		else:
			print(r.text)
		# print("random seller", random_seller)
		# print("ffffff>>>",random_category[0],random_item[0], random_seller)


print(random_date_gen())
create_order_table(n=1)