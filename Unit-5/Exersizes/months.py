while True:
    month = input("Enter a month: ").lower().capitalize()

    match month:
        case "January"|"March"|"May"|"July"|"September"|"November":
            print(f"{month} has 31 days")

        case "Feb" | "Febuary":
            print("Febuary has 28 or 29 days")

        case "April"|"June"|"August"|"October"|"December":
            print(f"{month} has 30 days")

        case _:
            print("Please enter a valid month")
            continue

    cont = input("Would you like to try again?(y/n): ").lower()
    if cont == "y":
        continue
    else:
        break

print("Bye!")