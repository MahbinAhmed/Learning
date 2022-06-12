class Student :
    def __init__(self,name,age,clas):
        self.name = name
        self.age = age
        self.clas = clas

    def print_details(self):
        return f"Your name is {self.name}, your age is {self.age}, you are in class {self.clas}"

Alex = Student("ALex",10,5)
John = Student("John",14,8)

# Alex.name = "Alex"
# Alex.age = 10
# Alex.clas = 5
#
# John.name = "John"
# John.age = 14
# John.clas = 8

print(Alex.age)
# print(Alex.print_details())

