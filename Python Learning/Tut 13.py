s1 = set([1,2,3,5]) # It's a set
s2 = {6,7,9,4} # It's also a set
s1.add(9)
si= s1.union(s1,s2) # It's used to union something in set
s2.remove(6)
print(s1)
print(s2)
print(si)
print(len(s1))
print(max(s1))
print(min(s1))
print(type(s1))