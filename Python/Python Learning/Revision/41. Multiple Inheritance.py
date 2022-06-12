# Multiple Inheritance

class Student:
    a = 10
    def __init__(self,name,roll) -> None:
        self.name = name
        self.roll = roll

    def print_std_details(self):
        return f"This is from Student class. Name is {self.name}, roll is {self.roll}"

class Player:
    a = 9
    def __init__(self,name,game_name,age) -> None:
        self.name = name 
        self.g_name = game_name
        self.age = age

    def print_plr_details(self):
        return f"This is from Player class. Name is {self.name}, player of {self.g_name} and age is {self.age}"

class Smart_Programmer(Student,Player):
    a = 8

John = Smart_Programmer("John",15)
print(John.print_std_details())
print(John.a)