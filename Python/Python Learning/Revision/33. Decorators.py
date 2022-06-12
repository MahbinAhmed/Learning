# Decorators

# def func1(a):
#     a("First line")

# func1(print)

def decorator1(function):
    def executor():
        print("Executing...")
        function()
        print("Executed")
    return executor

@decorator1
def sample_function():
    print("Hello World")

# decorator1(sample_function)
sample_function()