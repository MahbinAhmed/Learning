# Object Introspection

import inspect

class Student:
    def __init__(self,name) -> None:
        self.name = name

    def print_details(self):
        print(f"My name is {self.name}")

John = Student("John Cena")

print(type("Hello World"))
print(id("Hello World"))
print(dir("Hello World"))
print(inspect.getmembers(John))