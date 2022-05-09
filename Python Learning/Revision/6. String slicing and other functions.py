# String slicing

text = "A quick brown fox jumps over the lazy dogs"

print(text[0:5])
print(text[0:10:2])
print(text[::])
print(text[-5:-1])
print(text[::-1])

# Other string functions

print(text.capitalize())
print(text.casefold())
print(text.count("s"))
print(text.encode())
print(text.endswith("s"))
print(text.expandtabs())
print(text.zfill(50))
print(text.upper())
print(text.lower())
print(text.index("do"))
print(text.isalnum())
print(text.isupper())
print(text.replace("fox","cheetah"))
print(text.rfind("jumps"))