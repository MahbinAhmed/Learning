# Instance & Class variables

class Student:
    school = "Sherpur Government Victoria Academy"

Alex = Student()
John = Student()

Alex.name = "Alex"
Alex.cls = 7
John.name = "John"
John.cls = 8
print(Alex.name)
print(Alex.school)

# Student.school = "SGVA"
# print(Alex.school)
Alex.school = "SGVA"
print(Alex.school)
print(Student.school)
print(Alex.__dict__)