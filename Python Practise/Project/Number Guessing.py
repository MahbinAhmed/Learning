# Project:- Number guessing

# Importing Random Module
import random


# Taking input for number guessing range
print("Enter number range === \n")

while True:
    try:
        starting_number = int(input("Starting :- "))
        ending_number = int(input("Ending :- "))
        break
    
    except ValueError:
        print("Please enter a valid input.\n")
        starting_number = int(input("Starting :-"))
        ending_number = int(input("Ending :- "))
        # continue


# Generating random number
random_number = random.randint(starting_number,ending_number)

# User attempts to guess the correct number
attempts = 0

# Taking guesses from user and increasing attempts
while True:
    try:
        guess_input = int(input("Enter your guess :- "))

        if guess_input == random_number:
            print("You have entered the right number.")
            attempts += 1
            break

        elif guess_input < random_number:
            print("Please enter a larger number.")
            attempts +=1

        elif guess_input > random_number:
            print("Pleae enter a smaller numbr.")
            attempts +=1
    except:
        print("Please enter a valid input.")
        continue

# Showing result1
print(f"You have guessed the right number with only {attempts} attempts.")