# stock = {"Pizza": 15, "Burger": 5, "Soda": 0}

# for key, value in stock.items():
#     if value > 0:
#         print(f"{key} : {value} in stock")


lines = ["Pizza,250.0,15", "Burger,260.0,5", "Soda,20.0,25"]
menu_list = []
expensive = 0
count = 0
for product in lines:
    name , price , qty = product.split(",")
    menu = {
        'name': name,
        'price': float(price),
        'qty': int(qty)
    }
    menu_list.append(menu)
    if menu['qty'] > 10:
        count = count + 1
    if menu['price'] > expensive:
        expensive = menu['price']

for prod in menu_list:
    if expensive == prod['price']:
        print(f"{prod['name']} is the expensive one")
print(menu_list)
print(expensive)
print(f"count of product having more than 10 is {count}")