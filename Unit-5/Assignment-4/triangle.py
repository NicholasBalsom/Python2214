#Assuming correct user input
A = float(input("Enter side A: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))

if A == B == C:
    print("Equilateral")
elif A == B or A == C or B == C:
    print("Isosceles")
else:
    print("Scalene")