def is_palindrome(string):
    length = len(string)
    
    for i in range(length):
        if string[i] != string[length-i-1]:
            return False
    
    return True

def get_string():
    string = input("Enter a string: ")
    return string

string = get_string()
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
