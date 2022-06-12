# Getters

class Student:
    def __init__(self,name,age) -> None:
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.getter
    def age(self):
        return self

    @age.setter
    def age(self,new_age):
        self._age = new_age

John = Student("John Cena",18)
print(John.age)
John.age = 50
print(John.age)