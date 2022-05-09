try :
    f = open("1.txt")
except Exception as e:
    print(e)

else:
    print("This line will print if the except line don't run\n")
finally:
    print("The file can't be opened\n")

# print("This is the last line")