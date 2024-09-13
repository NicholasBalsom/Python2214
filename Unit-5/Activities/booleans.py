numCredits = int(input("Ent number of credits: "))
majorGPA = float(input("enter GPA for the major: "))
overallGPA = float(input("Enter overall GPA: "))

if numCredits >= 120 and majorGPA >= 2.0 and overallGPA >= 2.0:
    print("Congratulations!\You seem to meet all the criteria for graduation.")
else:
    print("Sorry!\You do not seem to meet all the criteria for graduation.")
print("done!")