while True:
    word = input("Whats the secret word: ")
    if word.lower() == "abracadabra":
        break
    else:
        print("Try again.\n")
print("You have sucsessfully exited the loop.")