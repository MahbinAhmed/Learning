# Operator overloading & Dunder methods

class Student:
    def __init__(self,name,number) -> None:
        self.name = name
        self.number = number

    def __add__(self, a):
        return self.number + a.number

    def __repr__(self) -> str:
        return "It's a class named \"Student\""

    def __str__(self) -> str:
        return "Hello World"

John = Student("John",500)
Harry = Student("Harry",400)
print(John + Harry)
print(John)
print(str(John))
print(repr(Harry))