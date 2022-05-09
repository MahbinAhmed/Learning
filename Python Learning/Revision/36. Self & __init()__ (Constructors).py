# Self & __init()__ (Constructors)

# class Student:
#     school = "SGVA"

#     def details(self):
#         return f"Your school name is {self.name}. You are in {self.cls}"

# Alex = Student()

# Alex.name = "Alex"
# Alex.cls = 7

# print(Alex.details())

class Student:

    def __init__(self,name,cls) -> None:
        self.name = name
        self.cls = cls

Alex = Student("Alex",7)
print(Alex.name)