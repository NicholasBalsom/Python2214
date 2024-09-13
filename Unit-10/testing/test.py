with open("demo.txt") as file:
    reader = file.readlines()
    for line in reader:
        print(line.rstrip())
    