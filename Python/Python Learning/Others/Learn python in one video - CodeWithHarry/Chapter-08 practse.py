# Chapter-08 practise
# Q1
# def maximum(num1, num2, num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if (num2>num3):
#             return num2
#         else:
#             return num3
#
# h = maximum(5,10,2)
# print("The highest number is ", h)
#
# Q2
# def c2f(cel):
#     a = (cel*(9/5))+32
#     return a
#
# c = 25
# f = c2f(c)
# print("Coverting result is  ", f)
#
# Q3
# print("Hello, ", end="")
# print("how ", end="")
# print("are ", end="")
# print("you ", end="")
# print("?", end="")
#
# Q5
# n=5
# for i in range(n):
#     print("*"*(n-i))
#
# Q6
# def i2c(inch):
#     a = inch*2.54
#     return a
#
# i = 10
# c = i2c(i)
# print(c)
#
# Q7
# def remove(str, word):
#     a = str.replace (word, "")
#     return a
#
# ak = "    Hello mr. world    "
# aw = remove (ak, "world")
# print(aw)
#
# Q8
def table(n):
    for i in range(1, 11):
        N=n*i
    return N
    
a=table(4)
print(a)
