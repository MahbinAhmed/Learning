num1 = (input("Enter a number \n"))
num2 = (input("Enter another number \n"))

try:       # It's used to handle errors
    print("The sum of these numbers is ", int(num2)+int(num1))
except Exception as e:
    print(e)