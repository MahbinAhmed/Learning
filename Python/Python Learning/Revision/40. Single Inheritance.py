# Single Inheritance

class Student:

    def __init__(self,name,roll) -> None:
        self.name = name
        self.roll = roll
    
    def print_std_details(self):
        return f"The name is {self.name}, roll is {self.roll} and printed from Student class"

class Programmer(Student):

    def __init__(self,name,roll,languages,post) -> None:
        self.name = name
        self.roll = roll
        self.languages = languages
        self.post = post

    def print_prog_details(self):
        return (f"Name is {self.name}, roll is {self.roll}, post is {self.post}")

Alex = Student("Alex",10)
John = Programmer("John",20,["Python","C","JavaScript"],"Prgrammer")
print(John.print_std_details())

# Code from CWH


# class Employee:
#     no_of_leaves = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


# class Programmer(Employee):
#     no_of_holiday = 56
#     def __init__(self, aname, asalary, arole, languages):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.languages = languages


#     def printprog(self):
#         return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")

# shubham = Programmer("Shubham", 555, "Programmer", ["python"])
# karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
# # print(karan.no_of_holiday)
# print(karan.printdetails())

