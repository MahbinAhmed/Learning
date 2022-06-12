# Problem-6

# Modules
import random


# Player_1_section
print("Player 1 turn :- ")

#Input_section_1
a = int(input("Enter the value of a :- "))
b = int(input("Enter the value of  b :- "))

# Random_number_generator_1
random_number = random.randint(a,b)

# Player_1_guesses

player_1_number_of_guesses = 1

while True:
    player_1_guess_input = int(input("Enter your guess :- "))
    if player_1_guess_input == random_number:
        print("You guessed the correct number !")
        break

    elif player_1_guess_input > random_number:
        print("Please enter a smaller one !")
        player_1_number_of_guesses += 1
        continue

    elif player_1_guess_input < random_number:
        print("Please enter a greater one !")
        player_1_number_of_guesses += 1
        continue

    else:
        print("Enter a valid input !")
        player_1_number_of_guesses += 1
        continue
print("\n\n")




# Player_2_section
print("Player 2 turn :- ")

# Input_section_2
a = int(input("Enter the value of a :- "))
b = int(input("Enter the value of b :- "))

# Random_number_generator_2
random_number = random.randint(a,b)

# Player_2_guesses
player_2_number_of_guesses = 1

while True:
    player_2_guess_input = int(input("Enter your guess :- "))

    if player_2_guess_input == random_number:
        print("You guessed the correct number !")
        break

    elif player_2_guess_input > random_number:
        print("Please enter a smaller one !")
        player_2_number_of_guesses += 1
        continue

    elif player_2_guess_input < random_number:
        print("Please enter a greater one !")
        player_2_number_of_guesses += 1
        continue

    else :
        print("Enter a valid input !")
        player_2_number_of_guesses += 1
        continue

print("\n\n")

# Final_result

print(f"Player 1 took {player_1_number_of_guesses} attempts to guess the correct answer.")
print(f"Player 2 took {player_2_number_of_guesses} attempts to guess the correct answer.")

if player_2_guess_input > player_1_number_of_guesses :
    print("So player 1 won this match.")

elif player_1_number_of_guesses > player_2_number_of_guesses:
    print("So player 2 won this match.")

elif player_1_number_of_guesses == player_2_number_of_guesses:
    print("Game tie.")

else:
    print("Error occurs !")