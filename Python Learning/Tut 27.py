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

o = open("1.txt", "r")
print(o.readline(),end="")
print(o.readline())
# a = o.read(3)
# print(a)

# a = o.read(3)
# print(a)
# o.close()

# for line in o :
#     print(line)