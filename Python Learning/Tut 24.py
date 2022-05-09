def add(a,b):
    """This function is used to add two numbers""" # It's a docstring
    sum = a + b
    # print(sum)
    return sum

i = add(5,8)
print(i)
print(add.__doc__)