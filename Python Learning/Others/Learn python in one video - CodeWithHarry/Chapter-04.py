# Chapter-04 (List, Tuples)

# Lists
# List are used with []

a= [2,5,8,7]
print(a)
print(a[1])
a[1]= 6
print(a)
b=[50, "Mahid", True, 40.5]
print(b)

# List slicing
fruits= ["Mango", "Banana", "Jack fruit", "Pine apple", "Straw Berry"]
print(fruits)
print(fruits[1:])
# List Functions
c= [5,78,4,5,452,9]
c.sort()
c.pop(1)
c.remove(452)
c.reverse()
c.insert(1, 12)
c.append(15)
# c [2]=1
print(c)

# Tuples
# Tuples are used with ()
# Typles cannot be changed or updated
x=(5,21,5,2,25,4)
print(x.count(5))
print(x.index(25))