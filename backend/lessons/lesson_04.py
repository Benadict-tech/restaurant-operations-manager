menu = ["Pizza", "Burger", "Brownie", "Soda", "Pasta"]
stock = [10, 0, 25, 3, 7]

for i in range(len(menu)):
    if stock[i] == 0 :
        print(f"OUT OF STOCK:{menu[i]}")
        continue
    if stock[i] <= 5:
        print(f"ALERT: restock {menu[i]}")
        break
    print(f"{menu[i]} - {stock[i]}")

buns = 0

while buns <= 50:
    buns = buns + 12
    print(buns)



    
        
    