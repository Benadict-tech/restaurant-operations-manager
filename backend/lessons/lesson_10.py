menu_items =[
    {"name":"Burger", "price": 300, "stock":5, "is_available":True},
    {"name":"Pizza", "price": 250, "stock":15, "is_available":True},
    {"name":"Soda", "price": 280, "stock":0, "is_available":True}
]

# product_names = [menu['name'] for menu in menu_items]

# print(product_names)

# out_of_stock_items = [menu['name'] for menu in menu_items if menu['stock'] == 0]

# print(out_of_stock_items)

inventory_map = {menu['name']:menu['stock'] for menu in menu_items}
print(inventory_map)

# sorted_products = sorted(menu_items,key = lambda p:p['price'])
# print(f"sorted_products: {sorted_products}")

# desc_sorted_products = sorted(menu_items,key = lambda p:p['price'],reverse = True)
# print(f"Desenting: {desc_sorted_products}")

# discounted_prices = [(menu['name'], f"{menu['price']* 0.9 :.2f}") for menu in menu_items]
# print(discounted_prices)
dictionary = {}
for menu in menu_items:
    dictionary[menu['name']]= menu['stock']

print(dictionary)