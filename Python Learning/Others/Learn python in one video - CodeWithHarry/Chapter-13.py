# Chapter-13 (Advanced Python 2)

# Lambda
# def func(a):
#     return a+5

# func = lambda a : a+5
# square = lambda a : a*a
# sum = lambda a,b : a*b

# c = 5
# print(func(c))
# print(square(c))
# print(sum(c,10))

# Join Method
# l = ["Monitor","Speakers",'Mouse', 'Hard Disk', 'Key board', 'Web Cam', "Proccessor"]
# a = ", ".join (l)
# print(a)
# print(type(a))

# Format Method (The older version of f string)
# name = "Mahid"
# surename = "Ahmed"
# school = "SGVA"

# fString = f"My name is {name} and my surename is {surename} and I read in {school} "
# print(fString)

# a = "My name is {} and my surename is {} and I read in {} ".format(name, surename, school)
# a = "My name is {1} and my surename is {2} and I read in {0} ".format(name, surename, school)
# print(a)

# Map Function
# def add(num):
#     return num+5

# l = [5, 14, 20]
# print(list(map(add,l)))

# Filter Function 
# def greaterthan5(num):
#     if (num>5):
#         return True
#     else :
#         return False

# l = [1,2,3,45,6,7,85,163,99,4]
# print(list(filter(greaterthan5,l)))

# Reduce Function
# from functools import reduce
# def add(a,b):
#     return a+b

# l = [1,2,3,4]
# print(reduce(add,l))