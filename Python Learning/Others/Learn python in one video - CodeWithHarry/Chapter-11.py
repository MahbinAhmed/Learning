# # Chapter-11 (Inheritance)


class Employee:
    Company = "Google"
    def salary(self):
        print(500)


class Programmer (Employee):
    Language = "Python"

    def salary(self):
        super().salary()
        print(1000)

    
class Youtuber (Employee):
    def salary(self):
        super().salary()
        print(1500)
    Workstation = "Youtube"

Mahid = Employee()
Prottoy = Programmer()
Shairin = Youtuber()


# print(Mahid.salary)
# print(Prottoy.Company)
# print(Shairin.Workstation)
# print(Shairin.Company)
# print(Shairin.salary)
# Shairin.salary()

        