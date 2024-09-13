print("\nTravel time calculator\n")

miles = int(input("Miles traveled: "))
speed = int(input("Miles per hour: "))
hours = miles / speed
minutes = miles % speed 

print(f"\nEstimated travel time.\nHours: {int(hours)}\nMinutes: {int(minutes)}")