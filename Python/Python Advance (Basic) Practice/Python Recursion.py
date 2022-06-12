def factorial(n):
    if n==1:
        return 1
    else:
        return factorial(n-1) * n

# print(factorial(5))

# 0 1 1 2 3 5 8 13
# 1 2 3 5 8 13

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))