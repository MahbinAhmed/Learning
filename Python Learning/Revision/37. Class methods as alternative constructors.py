# Class methods as alternative constructors


class Student:

    school_name  = "ABC High school "

    def __init__(self,name,roll) -> None:
        self.name = name
        self.roll  = roll

    @classmethod
    def object_from_str(cls, string):
        splitter = string.split("-")
        return cls(splitter[0],splitter[1])

    @classmethod
    def school_name_changer(cls,new_name):
        a = cls.school_name = new_name
        return a

Alex = Student.object_from_str("Alex-10")
print(Alex.roll)
print(Alex.school_name)
Alex.school_name_changer("BAC High school")
print(Alex.school_name)
print(Student.school_name)