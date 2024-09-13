small = int(input("Number of bottles less than or equal to 1L: "))
big = int(input("Number of bottles more than 1L: "))

refund = round((small * 0.10) + (big * 0.25), 2) 
print(f"Cash back: ${refund}")