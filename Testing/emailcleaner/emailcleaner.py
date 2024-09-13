import csv

print("Welcome to the Email List Cleaner")

source_file = input("Source csv file: ")
new_file = input("New csv file: ")
data = []

with open(source_file) as file:
    reader = csv.DictReader(file)
    for line in file:
        first_name, last_name, email = line.split(',')
        data.append([first_name, last_name, email])
    
print(data)
