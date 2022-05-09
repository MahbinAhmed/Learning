# Python Comprehensions

# List Comprehension

# lst = [i for i in range(50) if i%2==0]
# print(lst)

# Dictionary Comprehension

# dictionary = {i:f"item{i}" for i in range(10)}
# dictionary2 = {value:key for key,value in dictionary.items()}
# print(dictionary)
# print(dictionary2)

# Set Comprehension

# set1 = {foodNames for foodNames in ["Burger","Chicken","Burger","Sandwitch"]}
# print(set1)

# Generator Comprehension

# gen = (i for i in range(10) if i%2==0)
# print(gen.__next__())
# print(gen.__next__())