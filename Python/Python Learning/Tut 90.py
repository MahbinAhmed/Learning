a = input("Enter your name : ")
b = input("Enter a number : ")

if int(b)==0:
    raise IndexError("Enter a number bigger than 0")

if a.isnumeric():
    raise Exception("Enter your name not a number bro")