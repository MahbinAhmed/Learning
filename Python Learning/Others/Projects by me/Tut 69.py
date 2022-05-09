from abc import ABC,abstractmethod

class forced_class (ABC):
    @abstractmethod
    def print_details (self):
        return 0

class Student(forced_class):
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def print_details(self):
        return f"You'r name is {self.name}. You roll is {self.roll}"

    def adding(self):
        return 5+5

Alex = Student("Alex",5)
print(Alex.adding())

