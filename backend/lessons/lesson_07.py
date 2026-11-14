raw_name = " chicken BURGER "
chicken = raw_name.strip().title()
print(chicken)

order_line = "Burger,150.30,3"
name ,price, qty = order_line.split(",")
order = {
    "name":name,
    "price":float(price),
    "qty":int(qty)
}
print(order)



print(f"order : {order}")
qty = 3
item = "Chicken Burger" 
unit_price = 50.10 
total = 150.30
receipt_line = f"{qty} \u0078 {item} \u0040 \u20B9{unit_price:.2f} = \u20B9{total:.2f}"

print(f"reciept : {receipt_line}")

order_id = "ORD-1042"
print(order_id.startswith("ORD-"))

menu = ", ".join(["Pizza", "Burger", "Soda"])
print(menu)
