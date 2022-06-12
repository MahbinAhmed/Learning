# Super() and overriding classes

class A:
    class_var_1 = "Class variable of class A"

    def __init__(self) -> None:
        self.var = "Inside class A's constructor"
        self.class_var_1 = "Instance variable in class A"
        self.special_var = "Special Instance variable from class A"

class B(A):
    class_var_1 = "Class variable of class B"

    def __init__(self) -> None:
        super().__init__()
        self.var = "Inside class B's constructor"
        self.class_var_1 = "Instance variable in class B"

a = A()
b = B()
print(b.class_var_1)
print(b.special_var)