# Iterative approach

# def factorial_iterative(n):
#     a = 1
#     for i in range(n):
#         a = a * (i+1)
#     return a

# value_1 =  5
# print(factorial_iterative(value_1))

# Recursive approach

# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else :
#         a = factorial_recursive(n-1)
#         return n * a

# print(factorial_recursive(5))

# Fibonacci series

def fibonacci_series(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

print(fibonacci_series(7))