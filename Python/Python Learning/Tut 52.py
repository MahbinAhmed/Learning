# def func1():
#     print("Hello World")
# func2 = func1
# del func1
# func2()

# def function1(num):
#     return print
#
# print(function1(1))

# def executer(argument):
#     argument("Hello world")
#
# executer(print)


# Decorator
# @ Decorator

def dec1(function):
    def sub_function():
        print("Executiong")
        function()
        print("Executed")
    return sub_function()

@dec1
def printing():
    print("Hello world")
# # Decorator
# a = dec1(printing)
