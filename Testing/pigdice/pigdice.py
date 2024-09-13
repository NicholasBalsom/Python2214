print("Pig Dice Rules:")

with open('rules.txt') as file:
    for line in file:
        if line.startswith('*'):
            print(line.rstrip())
            