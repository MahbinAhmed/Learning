class Student:
    def __init__(self,name,age,mark):
        self.name = name
        self.age = age
        self.mark = mark

    @classmethod
    def single_line_input(cls, user_input):
        splitter = user_input.split("-")
        # return cls(splitter[0],splitter[1],splitter[2])
        return cls(*splitter)

David = Student.single_line_input("David-12-89")
print(David.age)
