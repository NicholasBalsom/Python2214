#Guessing game

import random

atempts = 0
answer = random.randint(1, 10)
guess = 0

while guess != answer:
    guess = int(input("Guess a number (1 to 10): "))

    if guess == answer:
        atempts += 1
        break
    elif guess > answer:
        atempts += 1
        print("Too high.")
    elif guess < answer and guess > 0:
        atempts += 1
        print("Too low.")
    else:
        print("invalid guess. Try again")
        
print(f"Correct! The answer was {answer}. You guessed it in {atempts} tries.")