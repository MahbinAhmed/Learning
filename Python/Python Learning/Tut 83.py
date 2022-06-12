import json

data = '{"Book":"A bundle of knowledge","Egg":"One kind of food"}'
# print(data)
# print(type(data))
persed = json.loads(data)

# print(type(persed))
print(persed["Book"])

dict = {"Name":"Alex","PC":"Personal computer","Network": True}
# print(dict)
dumping = json.dumps(dict, sort_keys=True)
# print(type(dumping))

print(dumping)