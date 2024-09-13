'''
MI1850/Python 2214 2022-23
Practicum Part 2
Nicholas Balsom
CBRH
'''

# **READ ME*** I didnt include the command input loop in the menu function but it does the same thing.


import os
import csv
from pathlib import Path
import time

subject_marks = []

def display_menu():
    print("""
___________________Menu Options___________________
1. Enter grades for a new subject
2. Calculate average for each subject,
3. Count failures (marks under 50) for all subject,
4. Write marks to CSV or text file,
5. Exit
""")
    

def enter_grades():
    marks = []
    marks.append(input("Subject name: "))
    while True:
        grade = input("Grade: ")
        try:
            if grade == "x":
                subject_marks.append(marks)
                break
            elif 100 >= float(grade) >= 0:
                marks.append(round(float(grade), 1))
            else:
                print("Invalid grade.")
        except ValueError:
            print("Invalid grade.")


def calculate_avg(subject):
    avg = 0
    # Find subject in subject_marks
    for i in range(len(subject_marks)):
        if subject_marks[i][0] == subject:
            # Calculate average
            for grade in subject_marks[i][1:]:
                avg += grade
            avg /= len(subject_marks[i][1:])
            return (f"Average for {subject} is {round(avg, 2)}")
    return ("Subject doesn't exsist.")


def count_fails():
    # Counts all failing grades in subject_marks
    count = 0
    for i in range(len(subject_marks)):
        for grade in subject_marks[i][1:]:
            if grade < 50:
                count += 1
    return (f"Total number of failures is {count}")


def write_to_file():
    # Gets current working directory
    dir = os.getcwd() 
    dir += "\marks.csv"
    with open(dir, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(subject_marks)
    # Check if file was created
    if Path(dir).exists():
        print("File was successfully created!")
    else:
        print("File could not be created.")


def main():
    # It was easier to have the commad loop in main() than in the display_menu() fuction.
    print("Welcome to Subject Grade Program")
    display_menu()
    while True:
        try:
            command = int(input("Enter the number corresponding to your choice: "))
        except ValueError:
            print("Invalid command. Try again.")
            continue
        if command == 1:
            enter_grades() 
        elif command == 2:
            print(calculate_avg(input("Subject: ")))
            time.sleep(1.5)
        elif command == 3:
            print(count_fails())
            time.sleep(1.5)
        elif command == 4:
            write_to_file()
            time.sleep(1.5)
        elif command == 5:
            print("Bye!")
            break
        else:
            print("Invalid command. Try again.")
        display_menu()


if __name__ == "__main__":
    main()
