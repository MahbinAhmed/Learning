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
f = open("1.txt")
# print(f.tell()) # It's used to detect to where is the pointer
print(f.readline())
print(f.tell())
# print(f.readline())
f.seek(10)
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.readline())
f.close()