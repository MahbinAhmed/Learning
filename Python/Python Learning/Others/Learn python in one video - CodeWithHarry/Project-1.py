# Project-01 (Snake, Water, Gun game)
# I will make Rock, paper, scissor game!!!

import random
def gamepro(sys,user):
    if sys==user:
        return None
    if sys== "r":
        if user=="p":
            return True
        if user=="s":
            return False
    if sys == "p":
        if user=="s":
            return True
        if user == "r":
            return False
    if sys == "s":
        if user == "r":
            return True
        if user == "p":
            return False        


print("Computer choose: Rock, paper, scissor")
rand = random.randint(1,3)
if rand == 1:
    computer = "r"
elif rand == 2:
    computer = "p"
elif rand == 3:
    computer= "s"
inp = input("Enter your choice ; Rock(r), paper(p), Scissor(s) ")
a=gamepro(computer,inp) 

print ("Computer choose :", computer)
print ("Your choose : ", inp)
if a == None:
    print("This game is tie!")
elif a== True:
    print("You won the game")
else :
    print("You lose the game")