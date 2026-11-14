

tax_rate = 0.05 

def broken_tax(amount):
    tax_rate = 0.10
    print(f"Tax inside : {tax_rate}")
    return amount * tax_rate

def good_tax(amount,rate):
    return amount * rate

good = good_tax(40000,tax_rate)
print(f"good tax : {good}")

broken_tax(20000)
print(f"Tax rate : {tax_rate}")

def show_special(item = "Chef's Special"):
    return f"Today: {item}"

print(show_special())
print(show_special("Pasta"))
tax_rate = 2
def mystery():
    return tax_rate + 10

print(mystery())