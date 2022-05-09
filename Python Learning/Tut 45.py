list = ["Alex","Harry","Rohan","John"]
# a = 1
# for item in list:
#     if a%2 != 0:
#         print(item)
#     a = a+1
for a,b in enumerate(list):
    if a%2==0:
        print(a,b)