class Student :
    school_name = "ABC high school"
    def __init__(self,name,age,Entering_year):
        self.name = name
        self.age = age
        self.year = Entering_year

    def print_student_details(self):
        return f"Hey there! I am student. My name is {self.name}. I am in {self.school_name}, I am {self.age} years old. I have joined this school in {self.year}."


class Player :
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def print_player_details(self):
        return f"Hey there! I am player. My name is {self.name}. I am a {self.game} player."


class Programmer(Student,Player):
    def __init__(self,name,age,entering_year,game):
        self.name = name
        self.age = age
        self.year = entering_year
        self.game = game

    def print_programmer_details(self):
        return f"Hey there! I am a programmer. My name is {self.name}. I was also a student and {self.game} player."


Alex = Student("Alex",15,2000)
Harry = Player("Harry","Cricket")
John = Programmer("John",25,2002,"Football")
print(John.print_programmer_details())
print(John.print_student_details())