stats = [48.0, 30.5, 20, 100.0, 15]
inventory = ["Bread", "Molassas", "Butter", "Meat"]

print(f"The stats list contains: {stats}\n")
print(f"The inventory list contains: {inventory}\n\n")

stats.append(45)
print(f"Line 7 {stats}\n")

inventory.insert(2, "Veggies")
inventory.insert(0, "Fruits")
print(f"Line 11 {inventory}\n")

stats.remove(30.5)
print(f"line 14 {stats}\n\n")

item = inventory.pop()
print(f"Line 17 {inventory}")
print(f"The item removed was: {item}\n\n")

item = inventory.pop(2)
print(f"Line 21 {inventory}")
print(f"The item removed was: {item}\n\n")

x = inventory.index("Fruits")
print(f"The variable x contains the position of 'Fruits' in the inventory list, which is position {x}\n")

inventory.pop(x)
print(f"Line 28 {inventory}")

