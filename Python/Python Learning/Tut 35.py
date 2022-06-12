# It's an iterative approach
# def facetorial(n):
#     fac = 1
#     for i in range (n):
#         fac =  fac * (i+1)
#     return fac
#
# number = int(input("Enter a number : "))
# print(facetorial(number))

# It's a recursive approach
# def recursive_factorial(a):
#     if a == 1 or a == 0:
#         return 1
#     else:
#         return a * recursive_factorial(a-1)
#
# user_input = int(input("Enter a number for recursive approach : "))
# print(recursive_factorial(user_input))

# Quiz
def recursive_fibonachi(x):
    if x== 1:
        return 0
    elif x == 2:
        return 1
    else:
        return recursive_fibonachi(x-1)+recursive_fibonachi(x-2)

user_input2 = int(input("Enter a number for recursive fibonachi : "))
print(recursive_fibonachi(user_input2))
