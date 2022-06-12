class Student :
    def __init__(self,name):
        self.name = name

    @staticmethod
    def print_something(name):
        return "You'r name is " + name


Harry = Student("Harry")

print(Harry.print_something("Harry"))