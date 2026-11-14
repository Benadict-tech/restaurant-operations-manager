menu = ["Pizza", "Burger", "Brownie", "Soda", "Pasta"]

menu.append("Prawn")

print(menu)

menu.insert(1,"Salad")

print(menu)

menu.remove("Soda")

print(menu)

print(menu[:3])

print(menu[-2:])

print("Burger" in menu)

menu.sort()
print(menu)

product = ("Pizza", 200.0, 10)

name,price,stock = product
print(f"Name: {name}, Price: {price}, Stock: {stock}")

# product[0] = "Wrap"
# TypeError: 'tuple' object does not support item assignment



