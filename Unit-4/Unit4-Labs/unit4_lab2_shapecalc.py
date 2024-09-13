print("Enter below the dimensions of a rectangular prism.\n")
units = input("Enter unit of measurment: ")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
height = float(input("Enter height: "))

print(f"The volume is: {round(length * width * height, 2)} {units}")