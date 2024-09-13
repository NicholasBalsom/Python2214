price = float(input("Price: "))
tax = float(input("Tax rate: ")) / 100
total = round(price * tax + price, 2)
print(f"The total price is {total}")