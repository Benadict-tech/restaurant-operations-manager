restaurant_name = "Deeps Cafe"
print(restaurant_name)

product_name = input("Enter the product name : ")
product_price = float(input("Enter the price : "))
product_quantity = int(input("Enter the quantity : "))
user_input_bool = input("Is it available? (yes/no): ")

is_available = user_input_bool in ("yes", "y", "true", "1")

if not is_available:
    print(f"Sorry {product_name} is out of stock")
else:
    subtotal = product_price * product_quantity

    if subtotal >= 1000:
        discount = 10
    elif subtotal >= 500:
        discount = 5
    else:
        discount = 0

    subtotal_with_discount = subtotal -  (subtotal * (discount/100))

    tax = subtotal_with_discount * 0.05

    total = subtotal_with_discount + tax
    
    print(f"The subtotal of {product_name} is {subtotal_with_discount:.2f} with discount of {discount}% and the tax is {tax:.2f} .Overall the total is {total:.2f}")

    if total >= 500 or product_quantity > 5:
        print("Customers get free delivery")

    delivery_box_quantity = 12

    full_box = product_quantity // delivery_box_quantity
    leftovers = product_quantity % delivery_box_quantity

    print(f"Full box: {full_box}")
    print(f"Leftovers: {leftovers}")



