# Raise in 

a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))

if a == 0 or b == 0:
    raise ZeroDivisionError("Please enter except 0")

else:
    print(f"{a}/{b}={a/b}")