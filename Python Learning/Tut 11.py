dict1 = {"David":"Egg","Smith":"Cutlet","Andrew":"Fish","Harry":{"Breakfast":"Bread","Lunch":"Rice","Dinner":"Soup"}} # It's a dictionary
dict1["Sam"]=["Chicken"] # It's used to add something in a dictionary
del dict1["Sam"] # It's used to remove something from a dictionary
dict1.update({"Alex":"Vegetables"}) # It's also used to add something in a dictionary
dict2 = dict1.copy() # This function is used to make a copy of a dictionary
del dict2["Smith"]
# print(dict1["Harry"]["Breakfast"])
print(dict1)
print(dict2)
print(dict1.items())
print(dict1.keys())