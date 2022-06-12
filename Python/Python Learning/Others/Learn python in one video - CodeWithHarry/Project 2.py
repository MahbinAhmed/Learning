# Project-02 (The perfect guess)
import random
randnum = random.randint(1,100)
print(randnum)
userguess = None
guesses = 0

while (userguess!=randnum):

    userguess = int (input("Enter your guess"))
    guesses = guesses+1

    if userguess==randnum:
        print("You guessed the right number\n")
    else :
        if (userguess<randnum):
            print("You guessed a smaller number than the answer. Please select a larger number")
        else:
            print("You guessed a larger number than the answer. Please select a smaller number \n")
        
print(f"You guessed the right number in {guesses} attempts ")

with open("highScore.txt","r")as f:
    hiscore = int(f.read())


if (guesses < hiscore):

    print("You have just broken the last high score!")
    
    with open("highScore.txt","w")as f:
        f.write(str(guesses))