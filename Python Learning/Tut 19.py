# i = 0
# while (True): # It's used to run the loop without any limit
#     if i<10:
#         i = i+1
#         continue
#     print(i)
#     i = i+1
#     if i == 20:
#         break     # It's used to stop the loop

#Quiz

while(True):
    a = int(input("Enter a number : "))
    if a <= 100:
        print("Enter a number that is grater than 100")
        continue
    else:
        print("Great")
        break
