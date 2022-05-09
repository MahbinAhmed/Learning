# Static methods

class Student:

    def __init__(self,name,roll) -> None:
        self.name = name
        self.roll = roll

    @staticmethod
    def print_function():
        print("Hello World")

Alex = Student("Alex",10)
Alex.print_function()