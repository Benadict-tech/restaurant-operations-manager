menu =[
    {"name":"Burger", "price": 300, "stock":5, "is_available":True},
    {"name":"Pizza", "price": 250, "stock":15, "is_available":True},
    {"name":"Soda", "price": 280, "stock":25, "is_available":True}
]
expensive = 0
total_value = 0
cat = set()
for product in menu:
    if product['name'] == "Burger":
        product['price'] = 210
    product['category'] = "Snack"
    

    if product['price'] > expensive:
        expensive = product['price']
    
    product_value = product["price"] * product["stock"]
    total_value += product_value
    
    # print(f"non existent : {product.get('shipping')}")
    cat.add(product['category'])
    print(f"{product['name']} — ₹{product['price']:.2f} — {product['stock']} in stock and its catogory is {product['category']}")

for prod in menu:
    if expensive == prod['price']:
        print(f"{prod['name']} is the expensive one")
print(f"expensive : {expensive}" )
print(f"total_value : {total_value}")
print(f"Set : {cat}")



