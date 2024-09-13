month = input("Enter month: ").lower().capitalize()
day = int(input("Enter day: "))

match month:
    case "January" | "Febuary":
        season = "Winter"

    case "March":
        if day < 20:
            season = "Winter"
        else:
            season = "Spring"

    case "April" | "May":
        season = "Spring"

    case "June":
        if day < 20:
            season = "Spring"
        else:
            season = "Fall"

    case "July" | "August":
        season = "Fall"

#Not finished