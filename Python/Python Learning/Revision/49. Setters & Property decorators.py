# Setters & Property decorators

class Employee:
    def __init__(self,name,sure_name) -> None:
        self.name = name
        self.surename = sure_name

    def print_details(self):
        return f"My first name is {self.name} and my sure name is {self.surename}"

    @property
    def email(self):
        if self.name == None or self.surename == None:
            return "Email not seted."
        return f"{self.name}.{self.surename}@gmail.com"

    @email.setter
    def email(self,new_email_address):
        splitter = new_email_address.split("@")[0]
        self.name = splitter.split(".")[0]
        self.surename = splitter.split(".")[1]

    @email.deleter
    def email(self):
        self.name = None
        self.surename = None

John = Employee("John","Cena")
# print(John.email)

John.email = "Cena.John@gmail.com"
print(John.name)
print(John.surename)

del John.email

print(John.email)