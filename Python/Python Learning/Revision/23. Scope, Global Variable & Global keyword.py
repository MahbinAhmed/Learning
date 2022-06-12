# Scope, Global Variable & Global keyword

a = 5 # Global
c = 20 # Global

def function():
    a = 10 # Local
    b = 15 # Local

    global d # Global keyword
    d = 50
    global c # To get the permission for change the value of c
    c = c + 15

    print(a)
    print(c)

function()
print(a)
# print(b)
print(d)