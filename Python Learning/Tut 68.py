class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    def __add__(self, other):
        return self.mark + other.mark

s1 = Student("Student 1",50)
s2 = Student("Student 2",62)
a = s1 + s2
print(a)