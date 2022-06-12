# l = 10 # It's a global variable
#
# def function():
#     # l = 5 # It's a local variable
#     m = 8
#     global l # It's used to change the value of global variable
#     l = l + 8
#     print(l,m)
#     return
#
# print(l)
# a = function()
# print(a)

def ben():
    x = 20
    def alex():
        global x
        x = 88
    print("Before calling Rohan",x)
    alex()
    print("After calling Rohan",x)

ben()
print(x)