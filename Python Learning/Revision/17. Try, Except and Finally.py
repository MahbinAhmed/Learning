# Try, Except & Finally

try:
    input1 = int(input("Enter first number :- "))
    input2 = int(input("Enter second number :- "))
    print("Your result is ",input1+input2)
except:
    print("Error occured")
else:
    print("No error was occured")
finally:
    print("The programme has ended")