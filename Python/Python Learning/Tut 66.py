class A:
    variable1 = "It's the var 1 of class A"
    def __init__(self):
        self.var1 = "Hello this is var 1 of construtor class B"
        self.check = "This is checker for class A instance constructor"
        self.checker =  "Thsi is the second checker for class A instance constructor"
class B(A):
    variable2 = "It's the var 2 of class B"
    def __init__():
        super().__init__()
        self.var1 = "Hello this is var 1 of contruct in class B"
        self.check = "This is checker for class B instance constructor"
        # super().__init__()

Alex = B()
print(Alex.check)