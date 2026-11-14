from billing import calculate_total
import random

restaurant_name = "Deeps Cafe"
print(restaurant_name)

product_name = input("Enter the product name : ")
product_price = float(input("Enter the price : "))
product_quantity = int(input("Enter the quantity : "))
user_input_bool = input("Is it available? (yes/no): ")

is_available = user_input_bool in ("yes", "y", "true", "1")


def print_receipt(product_name,discounted_amount,discount_rate,tax,total):
    print(f"The subtotal of {product_name} is {discounted_amount:.2f} with discount of {discount_rate * 100}% and the tax is {tax:.2f} .Overall the total is {total:.2f}")


if not is_available:
    print(f"Sorry {product_name} is out of stock")
else:
    subtotal = product_price * product_quantity

    total, tax,discounted_amount,discount_rate = calculate_total(subtotal)
    
    print_receipt(product_name,discounted_amount,discount_rate,tax,total)

    if total >= 500 or product_quantity > 5:
        print("Customers get free delivery")

    delivery_box_quantity = 12

    full_box = product_quantity // delivery_box_quantity
    leftovers = product_quantity % delivery_box_quantity

    print(f"Full box: {full_box}")
    print(f"Leftovers: {leftovers}")
    print(f"Order #{random.randint(1000, 9999)}")





