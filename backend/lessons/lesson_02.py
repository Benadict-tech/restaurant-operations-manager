restaurant_name = "Deeps Cafe"

product_name = input("Enter the product name : ")
product_price = float(input("Enter the price : "))
product_quantity = int(input("Enter the quantity : "))

subtotal = product_price * product_quantity

tax = subtotal * 0.05

total = subtotal + tax
print(restaurant_name)
print(f"The subtotal of {product_name} is {subtotal:.2f} and the tax is {tax:.2f} .Overall the total is {total:.2f}")

if total >= 500 and product_quantity >= 2:
    print("Customers get free delivery")

delivery_box_quantity = 12

full_box = product_quantity // delivery_box_quantity
leftovers = product_quantity % delivery_box_quantity

print(f"Full box: {full_box}")
print(f"Leftovers: {leftovers}")

