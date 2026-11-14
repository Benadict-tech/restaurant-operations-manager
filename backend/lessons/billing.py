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

if __name__ == "__main__":
    print(calculate_total(1500))
    print(calculate_total(600))
    print(calculate_total(100))