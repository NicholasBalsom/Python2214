print("\nPrice Comparison\n")

pricelg = float(input("Price of 64oz size: "))
pricesm = float(input("Price of 32oz size: "))

print(f"\nPrice per oz (64oz): {round(pricelg / 64, 2)}")
print(f"Price per oz (32oz): {round(pricesm / 32, 2)}")