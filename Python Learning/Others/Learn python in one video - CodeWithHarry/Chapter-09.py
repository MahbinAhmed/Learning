# Chapter-09 (File I/O)
# f = open("Text.txt","r")
# # data = f.readline()
# data = f.read()
# print(data)
# f.close()

# a = open("Anoter.txt","a")
# b = a.write("That's an appending line")
# a.close()

with open("Text.txt","r") as f:
    print(f.read())