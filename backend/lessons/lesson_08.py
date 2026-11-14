restaurant_name = "Deeps Cafe"
print(restaurant_name)

product_name = input("Enter the product name : ")
product_price = float(input("Enter the price : "))
product_quantity = int(input("Enter the quantity : "))
user_input_bool = input("Is it available? (yes/no): ")

is_available = user_input_bool in ("yes", "y", "true", "1")

def calculate_discount_rate(subtotal):
    if subtotal >= 1000:
        return 0.10
    elif subtotal >= 500:
        return 0.05
    else:
        return  0.0

def calculate_discounted_subtotal(subtotal,discount_rate):
    return subtotal -  (subtotal * discount_rate)


def calculate_tax(amount,rate = 0.05):
    return amount * rate

def calculate_total(subtotal):
    discount_rate = calculate_discount_rate(subtotal)
    discounted_amount = calculate_discounted_subtotal(subtotal,discount_rate)
    tax = calculate_tax(discounted_amount)
    return discounted_amount + tax, tax, discounted_amount , discount_rate

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

print(calculate_total(1500))
print(calculate_total(600))
print(calculate_total(100))



