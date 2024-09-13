# Checks whether a number is even or odd using functions

print("Even or odd checker \n")
def main():
    if is_even(int(input("Enter whole number: "))):
        print("This number is even")
    else:
        print("This number is odd")


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()
