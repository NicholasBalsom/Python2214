print("Registration Form.\n")

firstname = input("First name:\t")
lastname = input("Last name:\t")
birthyear = input("Birth year:\t")

print(f"\nWelcome {firstname} {lastname}!\nYour registration is complete.\nYour temporary password is: {firstname}*{birthyear}")