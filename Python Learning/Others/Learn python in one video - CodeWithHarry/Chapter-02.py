#Chapter-02 (Variable,Datatypes)
"""Different kinds of datatypes :
01.str(String) [Can write with 'single quote, "double quote and '''triple codes. ''' Triple code 
                is necessecary to create a multi-line string]
02.int(Intiger) [Numbers]
03.float(Floating) [Number with decimals]
04.Booleans [Only contains True and False] """

a="Hello World"
b= 50
c= 50.5

print(type(a))
print(type(b))
print(type(c))

# Operators

# Arethmetic Operator
print("The rusult of 1+2 is", 1+2)
print("The rusult of 1-2 is", 1-2)
print("The rusult of 1*2 is", 1*2)
print("The rusult of 1/2 is", 1/2)

# Assignment Operator
a = 50
a += 10
a -= 10
a *= 10
a /= 10
print(a)

#Comparison Operator
x=(4>5)
y=(4<5)
print(x)
print(y)

# Logical Operator
bool1 = True
bool2 = False

print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The opposite bool2 is", (not bool2))

# Typecasting

k="505"
k=int(k)
print(k+5)

# Input
in1 = input("Enter a number:")
in1 = int(in1)
print(type(in1))
print(in1)