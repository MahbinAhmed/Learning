"""File IO Basics
File opening modes
1."r" = Open file for reading - default
2."w" = Open file for writing
3."x" = Creates file if not exists
4."a" = Add more content to a file
5."t" = Text mode - default
6."b" = Binary mode
7."+" = Read and write
"""

f = open("1.txt","a")
a = f.write("Hello World\n")
print(a)
f.close()

b = open("2.txt","r+")
print(b.read())
b.write("Hello World,\n this the second txt file")