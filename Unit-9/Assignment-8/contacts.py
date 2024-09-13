
contacts = [["Bob the Builder", "bob@builders.com", "+1(420)640-6969" ], 
            ["Eric Idle", "eric@ericidle.com", "+44(207)946-0958"]]

def display_title():
    print("\nContact Manager\n")


def display_commands():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")


def list():
    count = 1
    for name in contacts:
        print(f"{count}. {name[0]}")
        count += 1


def view():
    while True:
        num = input("Number: ")
        if num.isdigit(): 
            num = int(num)
            if 0 < num <= len(contacts):
                print(f"Name: {contacts[num-1][0]}")
                print(f"Email: {contacts[num-1][1]}")
                print(f"Phone: {contacts[num-1][2]}")
                break
            else:
                print("Contact doesn't exist")
                break
        else:
            print("Invalid input")         
    
    #Another way

    # while True:
    #     try:
    #         num = int(input("Number: "))
    #         break
    #     except ValueError:
    #         print("Not a number")

    # if 0 < num <= len(contacts):
    #     print(f"Name: {contacts[num-1][0]}")
    #     print(f"Email: {contacts[num-1][1]}")
    #     print(f"Phone: {contacts[num-1][2]}")
    # else:
    #     print("Contact doesn't exist")


def add():
    new_contact = []
    new_contact.append(input("Name: "))
    new_contact.append(input("Email: "))
    new_contact.append(input("Email: "))
    contacts.append(new_contact)


def delete():
    while True:
        num = input("Number: ")
        if num.isdigit():
            num = int(num)
            if 0 < num <= len(contacts):
                deleted_contact = contacts.pop(num-1)
                return deleted_contact[0]
            else:
                print("Contact doesn't exist")
                return "Error"
        else:
            print("Invalid input")

    # while True:
    #     try:
    #         num = int(input("Number: "))
    #         break
    #     except ValueError:
    #         print("Not a number")

    # if 0 < num <= len(contacts):
    #     deleted_contact = contacts.pop(num-1)
    #     return deleted_contact[0]
    # else:
    #     print("Contact doesn't exist")
    #     return "Error"


def main():
    display_title()
    display_commands()
    while True:
        command = input("\nCommand: ")
        if command == "list":
            list()
        elif command == "view":
            view()
        elif command == "add":
            add()
            print(f"{contacts[-1][0]} was added.")
        elif command == "del":
            deleted_contact = delete()
            if not deleted_contact == "Error":
                print(f"{deleted_contact} was deleted.")
        elif command == "exit":
            print("\nBYE!")
            break
        else:
            print("Command does not exist")


if __name__ == "__main__":
    main()