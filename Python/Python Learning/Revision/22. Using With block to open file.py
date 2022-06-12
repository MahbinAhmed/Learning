# With block for open file

with open("Random text 2.txt")as f:
    print(f.read())

f = open("Random text 2.txt")
print(f.readlines())