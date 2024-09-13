from random import randint

password = ""
with open("C:/Users/nbalsom_s/OneDrive/CompSci/School/Level 2/Unit-10/Labs/words.txt", "r") as file:
    reader = file.readlines()
    for i in range(2):
        password += reader[randint(1, len(reader))].rstrip().capitalize()
        
if 8 <= len(password) <= 10:
    print(password)