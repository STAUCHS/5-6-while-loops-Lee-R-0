# Example 4 - Guessing Game - Correct Solution
import random

#Generate number
random_num = random.randrange(1, 101)

#Ask user for their guess
guess = int(input("Guess a number: "))

#Create while loop
while guess != random_num:
    if guess > random_num:
        print("Guess is too high, try again!")
    else:
        print("Guess is too low, guess again!")

    guess = int(input("Enter a guess"))

print("That is the correct number!")