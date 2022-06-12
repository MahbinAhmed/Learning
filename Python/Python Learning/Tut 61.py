class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        return f"Student's name is {self.name} and his age is {self.age} years."

Rohan = Student("Rohan",15)
print(Rohan.print_info())

class ex_student(Student):

    def __init__(self,name,age,leave_year):
        self.name = name
        self.age = age
        self.leave_year = leave_year

    def print_ex_info(self):
        return f"Ex. student's name is {self.name} and his age is {self.age} years. He leaves the school in {self.leave_year}"

Harry = ex_student("Harry",18,2018)
print(Harry.print_ex_info())
