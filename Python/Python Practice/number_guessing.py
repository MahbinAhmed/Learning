# Trial project - Number guessing

import time
import random

random_number = random.randint(1,100)
player_point = 0
attempt_counter = 0

print("Welcome to number guessing challenge. You will get 10 chance to guess the correct number!\n")
while attempt_counter <=10:
    print(f"Currect time : {time.asctime()}")
    user_input = int(input("Enter your guess : "))
    if user_input<random_number:
        print("Please enter larger number!")
        attempt_counter += 1
        print(f"You have only {10-attempt_counter} attempts remaing !\n")
        continue
    elif user_input>random_number:
        print("Please enter lower number!")
        attempt_counter += 1
        print(f"You have only {10-attempt_counter} attempts remaining !\n")
        continue
    else:
        print("\nCongratulations! You have guessed the correct number.\n")
        attempt_counter += 1
        break

print(f"You have took {attempt_counter} attempt")