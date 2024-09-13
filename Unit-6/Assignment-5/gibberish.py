print("Gibberish Generator")

word = input("Enter starting word: ")
characters = input("Enter extra character(s) to insert: ")
gibberish = ''

for c in word:
    gibberish += c + characters
print(f"Gibberish word: {gibberish}")