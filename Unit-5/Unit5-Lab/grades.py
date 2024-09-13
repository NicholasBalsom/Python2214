while True:
    grade = int(input("Grade recieved: "))
    if grade > 100 or grade < 0:
        print("\nInvalid grade. Please try again.\n")
        continue
    else:
        break

if grade >= 80:
    letter = "A"  
elif grade >= 65:
    letter = "B"  
elif grade >= 55:
    letter = "C"
elif grade >= 50:
    letter = "D"
else:
    letter = "F"

print(f"Corresponding letter: {letter}\n")