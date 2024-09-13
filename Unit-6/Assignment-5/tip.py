meal_cost = float(input("Cost of meal?: "))

for i in range(15, 26, 5):  #range(start, stop, step)
    tip = round(meal_cost * (i / 100), 2)
    total = meal_cost + tip
    print(f"{i}% \nTip amount: ${tip:.2f} \nTotal amount: ${total:.2f} \n", end="")