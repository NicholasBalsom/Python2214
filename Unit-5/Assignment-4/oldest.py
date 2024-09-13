#Assumuing User enters correct information
person1 = int(input("Enter 1st age: "))
person2 = int(input("Enter 2nd age: "))
person3 = int(input("Enter 3rd age: "))

if person1 > person2:
    if person1 > person3:
        oldest = person1
    else:
        oldest = person3

elif person2 > person1:
    if person2 > person3:
        oldest = person2 
    else:
        oldest = person3

elif person3 > person1:
    if person3 > person2:
        oldest = person3
    else:
        oldest = person2
        
print(f"{oldest} is the oldest")