# Diamond shape problem in multiple inheritance

class A:
    def sample(self):
        print("Method from class A")

class B(A):
    def sample(self):
        print("Method from class B")

class C(A):
    def sample(self):
        print("Method from class C")

class D(B,C):
    def sample(self):
        print("Method from class D")

a = A()
b = B()
c = C()
d = D()

d.sample()