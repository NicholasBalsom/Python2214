# Converts the number of miles that you walked on a hike to the number of feet that you walked.

print("Hike calculator")
def main():
    miles_walked = float(input("How many miles did you walk?: "))
    feet = convert(miles_walked)
    print(f"You walked {feet} feet.")


def convert(miles):
    feet = round(miles * 5280, 2)
    return feet

if __name__ == "__main__":
    main()