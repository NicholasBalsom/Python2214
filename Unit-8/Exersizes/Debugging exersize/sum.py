def sum_even_numbers():
    sum = 0
    num_numbers = int(input("Enter the number of numbers: "))
    
    for i in range(num_numbers):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            sum += number
    return sum
    
    

def main():
    result = sum_even_numbers()
    print("The sum of the even numbers is:", result)

main()
