# Interesting-Game-with-Python
import random
randNumber = random.randint(1,50)
# print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if (userGuess == randNumber):
        print("You Gussed it right!")
    else:
        if (userGuess>randNumber):
            print(f"You Gussed it wrong. Guess a smaller number than {userGuess}.")
        else:
            print(f"You Gussed it wrong. Guess a larger number than {userGuess}.")


print(f"You guessed the number in {guesses}")
