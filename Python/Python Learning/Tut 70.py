class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}{lname}@gmail.com"

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return "Email is not available"

        return f"{self.fname}{self.lname}@gmail.com"

    @email.setter
    def email(self,new_email_name):
        names = new_email_name.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

Alex = Employee("Alex","Carry")
print(Alex.email)
Alex.fname = "Alax"
print(Alex.email)
Alex.email = "Carry.new@gmail.com"
print(Alex.email)
print(Alex.fname)
del Alex.email
print(Alex.email)