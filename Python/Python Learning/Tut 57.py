class Student:

    school_name = "ABC High School"

    def __init__(self,roll_no,mark):
        self.roll_no = roll_no
        self.mark = mark

    @classmethod
    def change_the_school_name(cls, new_name):
        cls.school_name = new_name


Starc = Student(5,85)
Starc.change_the_school_name("Code with Harry")
print(Student.school_name)
print(Starc.school_name)