
def display_title():
    print("The Wizard Inventory Program\n")


def display_commands():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")  
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit the program")


def show(inventory):
    count = 0
    for item in inventory:
        count += 1
        print(f"{count}. {item}")


def grab(inventory):
    if len(inventory) < 4:
        item = input("Name of item: ")
        inventory.append(item)
        print(f"{item} was added.")
    else:
        print("You can't carry any more items. Drop something first.")


def edit(inventory):
    if len(inventory) > 0:
        num = int(input("Number: "))
        if num <= len(inventory):
            inventory[num-1] = input("Updated name: ")
            print(f"Item number {num} was updated.")
        else:
            print("Invalid number")
    else:
        print("You don't have any items in your inventory to edit.")


def drop(inventory):
    if len(inventory) > 0:
        num = int(input("Number: "))
        if num <= len(inventory):
            item_dropped = inventory.pop(num-1)
            print(f"{item_dropped} was dropped.")
        else:
            print("Invalid number")
    else:
        print("You don't have any items in your inventory to drop.")  


def main():
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]
    display_title()
    display_commands()
    
    while True:  
        command = input("\nCommand: ").strip().lower()
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab(inventory)
        elif command == "edit":
            edit(inventory)
        elif command == "drop":
            drop(inventory)
        elif command == "exit":
            print("\nBye!")
            break
        else:
            print("Command does not exist")  


if __name__ == "__main__":
    main()