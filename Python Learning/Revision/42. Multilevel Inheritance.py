# Multilevel Inheritance

class GrandFather:
    study = 10
    poem = 1
    glass = 2

class Father(GrandFather):
    study = 15
    sports = 1
    glass = 3

class Son(Father):
    study = 20
    tech = 1

print(Son.study)
print(Son.poem)
print(Son.glass)