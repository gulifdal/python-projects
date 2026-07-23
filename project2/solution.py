# Project 2 Number Guessing Game
# Author: Gul Ifdal

import random

# 1. TODO: Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

# 2. TODO: Set up a guesses counter
attempts = 0

print("Welcome to the Number Guessing Game!")

# 3. TODO: Set up a loop to repeat until the user guesses correctly
while True:
    # 4. TODO: Get the user's guess (and increase counter)
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You found it in {attempts} attempts.")

        break































































