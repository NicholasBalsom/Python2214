#Calculates entry cost of a group based on age

cost = 0
while True:
    age = input("Enter age of guest (blank for none): ")
    if age == "":
        break
    
    age = int(age)

    if age <= 0:
        print("invalid age. Try again")
    elif age >= 3 and age <= 12:
        cost += 14
    elif age >= 65:
        cost += 18
    else:
        cost += 23
    continue

print(f"Entry cost: ${cost:.2f}")