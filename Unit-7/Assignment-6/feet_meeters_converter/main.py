import feet_meters_converter as convert


def display_title():
    print("=====Feet and meters converter===== \n")


def display_menu():
    print("Conversions Menu: \na. Feet to Meters \nb. Meters to Feet")


def main():
    conversion = input("Select a conversion (a/b): ").lower()
    if conversion == "a":
        feet = float(input("\nEnter feet: "))
        meters = convert.feet_to_meters(feet)
        print(f"{meters} meters\n")
    elif conversion == "b":
        meters = float(input("\nEnter meters: "))
        feet = convert.meters_to_feet(meters)
        print(f"{feet} feet\n")
    else:
        print("Invalid conversion. Please try again.")
        main()

    while True:
        cont = input("Would you like yo preform another conversion? (y/n): ").lower()
        if cont == "y":
            display_menu()
            main()
            break
        elif cont == "n":
            print("Thanks, bye!")
            break
        else:
            print("Invalid statement. Please try again.")
            continue


if __name__ == "__main__":
    display_title()
    display_menu()
    main()
