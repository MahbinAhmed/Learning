# Chapter-12 practise
# Q1
# def openFile(filename):
#     try:
#         with open(filename,"r")as f:
#             print (f.read())
#     except FileNotFoundError:
#         print(f"The file {filename} can't be open ")

# openFile("poem.txt")
# openFile("Highscore.txt")
# openFile("nothing.txt")

# Q2
# a= [1,2,3,4,5,6,7,8,9,10]
# for index, item in enumerate(a):
#     if index==1 or index==3 or index==5 or index==7 or index==9 :
#         print (item)   

# Q3
# num = int(input("Enter a number: "))
# table = [num*i for i in range(1,11)]
# print(table)

# Q4
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# try:
#     print(a/b)
# except:
#     print("Infinite")

# Q5
# num = int(input("Enter a number for multiplication table: "))
# table = [num*i for i in range(1, 11)]
# print(table)
# with open ("Table.txt","a")as f:
#     f.write(str(table))
#     f.write("\n")