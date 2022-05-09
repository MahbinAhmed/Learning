# Project :- Contact Book

import json

name_input = input("Enter your name :- ")
contact_input = input("Enter your contact name :- ")

dict1 = {name_input:contact_input}
with open("database.txt","r") as f:
    reader = json.load(f)
reader.update({name_input:contact_input})

with open("database.txt","a") as f:
    json.dump(reader,f)

# with open("database.txt","r")as f:
#     text_breaker = json.load(f)

# print(text_breaker["Hello"])