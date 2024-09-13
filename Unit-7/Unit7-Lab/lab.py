# ****UPDATED LAB****

import module_rectangle as rect
import random
import sys

def main():
    # Title 
    print('{:=^60s}'.format("Rectangle area and perimeter calculator"))

    descision = input("Would you like to use random dimensions? (y/n): ")
    if  descision== 'y':
        # Gets random integer from 1 to 100
        length = random.randint(1,100)
        width = random.randint(1,100)
        print(f"Length: {length}\nWidth: {width}")
    elif descision == "n":
        length = float(input("Enter length: "))
        width = float(input("Enter Width: "))
    else:
        sys.exit("Invalid input")
    
    units = input("Enter units (cm, m, ect.): ")
    area = rect.area(length, width)
    perimeter = rect.perimeter(length, width)
    print(f"Area: {area} {units}2")
    print(f"Perimeter: {perimeter} {units}")

if __name__ == "__main__":
    main()