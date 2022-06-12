class A:
    def checker(self):
        return "It's a checker from class A"

class B(A):
    def checker(self):
        return "It's a checker from class B"

class C(A):
    def checker(self):
        return "It's a checker from class C"

class D(B,C):
    def checker(self):
        return "It's a checker from class D"

a = D()
print(a.checker())