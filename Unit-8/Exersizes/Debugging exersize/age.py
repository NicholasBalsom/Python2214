def age_message(age):
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "You are a minor"
    elif age < 65:
        return "You are an adult"
    elif age > 65:
        return "You are a senior"

def get_age():
    age = input("Enter your age: ")
    return age

age = get_age()
message = age_message(int(age))
print(message)
