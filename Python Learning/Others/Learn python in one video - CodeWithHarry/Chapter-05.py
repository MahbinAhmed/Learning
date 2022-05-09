# Chapter-05 (Dictionary, Sets)

# Dictionary
# Dictionary are used {}
mydict={"Mahid":"It is a name of a person",
"Book":"A library of knowladge",
"Egg": "It is a food",
"anotherdic":{"Shairin": "It's also a name",
"Fahim":"It is a name also"}}
mydict["Egg"]="It is a kind of food"
# print(mydict["Egg"])
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())
# updatedict={"Mother":"In bangla ma"}
# mydict.update(updatedict)
# print(mydict)
# print(mydict["Mahid2"]) It will throw a error
# print(mydict.get("Mahid1")) #But it will show (none)

# Sets
a= set()
# print(type(a))
b={1,5,8,4,2,6}
# print(b)
b.add(9)
# print(b)
# print(b)
b.remove(8)
b.pop()
print(b)
print(len(b))
