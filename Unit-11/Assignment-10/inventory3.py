import random


def display_title():
    print("The Wizard Inventory Program\n")


def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")


def get_items():
    items = []
    with open("Unit-11/Assignment-10/all_items3.txt", 'r') as file:
        reader = file.readlines()
        for line in reader:
            items.append(line)
        return items


def get_inventory():
    try:
        with open("Unit-11/Assignment-10/inventory3.txt", "r") as file:
            reader = file.readlines()
            return reader
    except FileNotFoundError:
        print("\nCould not find inventory file.\n Starting with no inventory.")
        return []


def save(inventory):
    with open("Unit-11/Assignment-10/inventory3.txt", "w") as file:
        file.writelines(inventory)


def walk(inventory, items):
    num = random.randint(0, len(items)-1)
    print(f"While walking down a path, you see a {items[num]}")    
    if input("Do you want to grab it? (y/n): ") == "y":
        if len(inventory) < 4:
            inventory.append(items[num])
            print(f"You picked up a {items[num].rstrip()}") 
            save(inventory) 
        else:
            print("You can't carry any more items. Drop something first.") 


def show(inventory):
    count = 0
    if len(inventory) > 0:
        for item in inventory:
            count += 1
            print(f"{count}. {item.rstrip()}")
    else:
        print("Empty")


def drop(inventory):
    if len(inventory) > 0:
        try:
            num = int(input("Number: "))
            item_dropped = inventory.pop(num-1)
        except (ValueError, IndexError):
            print("Invalid item number")
            return
        print(f"{item_dropped.rstrip()} was dropped.")
        save(inventory)
    else:
        print("You don't have any items in your inventory to drop")
    

def main():
    display_title()
    display_menu()
    items = get_items()
    inventory = get_inventory()
    while True:
        command = input("\nCommand: ").lower()
        if command == "walk":
            walk(inventory, items)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop(inventory)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()