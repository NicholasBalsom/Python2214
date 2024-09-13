def display_title():
    print("Prime number checker.")


def is_prime(factors, num):
    if factors == [1, num]: # if the factors are equal to 1 and its self, it is prime
        return True

    
def get_factors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0: # If the number is divisible by i add i to the factors list
            factors.append(i)
    return factors


def main():
    display_title()
    while True:
        num = int(input("Enter a integer between 1 and 5000: "))
        if 1 <= num <= 5000:
            factors = get_factors(num)
            if is_prime(factors, num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is NOT a prime number.")
                print(f"It has {len(factors)} factors:",  *factors, sep=' ')
        else:
            print("Invalid input.")
            continue

        if input("Would you like to continue (y/n): ") == "n":
            print("\nBye!")
            break 


if __name__ == "__main__":
    main()