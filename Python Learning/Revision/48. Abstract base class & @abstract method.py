# Abstract base class & @abstractclassmethod

from abc import ABC,abstractclassmethod

class Base_class(ABC):

    @abstractclassmethod
    def print_details(self):
        return 1

class Student(Base_class):

    def name(self):
        return "Hello World"

    def print_details(self):
        return "It's from print details function in Student class"

John = Student()
print(John.name())