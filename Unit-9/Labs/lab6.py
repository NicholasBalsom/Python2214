from random import randint

def get_numbers():
    nums = []
    while True:
        n = randint(1, 49) # Get random int
        if not n in nums: # if the number isnt already in the list add the number
            nums.append(n)
            
        if len(nums) == 6:
            return nums


def main():
    nums = get_numbers()
    nums.sort()
    print(*nums, sep=' ') # Print the list, each value separated by a space


if __name__ == "__main__":
    main()