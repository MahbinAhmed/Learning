# Json Module

import json

# dump,dumps - Converting from python dictionary to json string
# load,loads - Converting from json string to python dictionary

data1 = '{"Name":"Alex","Age":50,"Profession":"Programmer"}'
ldata = json.loads(data1)
# print(data1)
print(ldata["Age"])

# data2 = {"Name":"Alex","Age":50,"Profession":"Programmer",}
# print(data2["Age"])
# ddata = json.dumps(data2, indent=1,separators=(". "))
# print(ddata) 
# print(type(ddata))

# json.load()
# json.dump()