# Chapter-12 (Advanced Python 1)

# Try
# while(True):
#     print("Enter q to exit the programme")

#     a = input("Enter a number: ")

#     if a == "q":
#         break
#     try:
#         a = int(a)    
#         if a>6:
#             print("You entered a number greater than 6")
#     except Exception as e :
#         print(f"Your input has an error: {e}")

# print ("You have completed the programme")


# Handling different types of error 
# try:
#     a = int(input("Enter a number: "))
#     b = 50/a
#     print(b)
# except ValueError as e :
#     print ("It's the error no 1")
#     print (e)

# except ZeroDivisionError as e :
#     print ("It's the error no 2")
#     print (e)

# # Raising custom error 
# def add (num):
#     try :
#        return int(num) + 1
#     except :
#         raise ValueError ("You 5entered a wrong value")

# a = add ("5d") 
# print(a)

# else clause
# try:
#     a = int(input("Enter a number: "))
#     b = 50 + a
#     print (b)
# except ValueError as e:
#     print("You have an error: ",e)

# else:
#     print("We have done it succesfully")

# Try_except_finally
# try:
#     a = int(input("Enter a number: "))
#     b = 50 + a
#     print (b)
# except ValueError as e:
#     print("You have an error: ",e)

# finally:
#     print("It's the finally line")

# if __name__ == "__main__":

# Global varieable_Local Varieable
# a = 50
# def function():
#     global a
#     print("This is the global a ",a)
#     a = 8
#     print("It is the local a ",a)
    
# function()
# print("This is also the local a", a)

# Enumerate function
# list = [5, 14, "Mahid"]
# index = 0
# for item, index in enumerate(list):
#     print(item, index)

# List comprehension
# a = [2, 4, 5, 8, 7 ,50, 55]
# # b = []
# # for item in a:
# #     if item%2==0:
# #         b.append(item)
# # print(b)
# b= [i for i in a if i%2==0]
# print(b)