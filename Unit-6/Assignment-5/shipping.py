print("=====================\n Shipping Calculator \n=====================")

shipping = 0

while True:
    cost = float(input("Cost of items ordered: "))
    if cost < 0:
        print("You must enter a positive number. Please try again.")
        continue
    elif cost < 30:
        shipping = 5.95
    elif cost >= 30 and cost < 50:
        shipping = 7.95
    elif cost >= 50 and cost < 75:
        shipping = 9.95
    else:
        shipping = 0
    print(f"Shipping cost: ${shipping:.2f} \nTotal cost: ${(cost + shipping):.2f}")

    cont = input("Continue (y/n): ")

    if cont.lower() == "y":
        print("")
        continue
    else:
        print("\nBye!")
        break
