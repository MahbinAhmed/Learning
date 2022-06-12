# for i in range(1,16):
#     if i%3 ==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0:
#         print("Fizz")
#     else:
#         print(i)

# text = "Hello World"
# # print(text[::-1])
# first_list = []
# for i in text:
#     first_list.append(i)
# first_list.reverse()
# print("".join(first_list))

# print(20//8)

# def reverse(s):
#   str = ""
#   for i in s:
#     str = i + str
#   return str

# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]

# print(reverse("Hello World"))

# def reverse(string):
#     string = "".join(reversed(string))
#     return string

# print(reverse("Hello World"))

# s = "hello world"

# string = "Hello Wolrd"
# # string = "".join(string)
# print(list(reversed(string)))










# <<<<<----- Final ----->>>>>

string = "Hello World"

# 1 --->>>
# print(string[::-1])

# 2 --->>>
# a = "".join(list(reversed(string)))
# print(a)

# 3 --->>>
# str = ""
# for i in string:
#     str = i + str

# print(str)

# 4 --->>>
# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]

# print(reverse(string))

# 5 --->>>
list1 = []
for i in string:
    list1.append(i)
list1.reverse()
a = "".join(list1)
print(a)