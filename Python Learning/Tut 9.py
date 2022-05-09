mystr = "Hello World"
print(mystr[4])
print(mystr[0:5])
print(len(mystr))
print(mystr[0:5:2])
print(mystr[-4:-1])
print(mystr[::-1])

print(mystr.isalnum()) # " --.isalnum " It's used to check the presence of space in a string
print(mystr.isalpha()) # "--.isalpha " It's also used to check the presence of space in a string
print(mystr.endswith("World")) # It's used to check the last letter or word in a string
print(mystr.count("l")) # It's used to count a letter or a word in a string

mystr2 = "hello World"
print(mystr2.capitalize()) # It's used to capitalize the first letter of a line
print(mystr2.find("lo")) # It's used to find anything in string
print(mystr2.lower()) # It's used to convert all the letter of a string to lower case
print(mystr2.upper()) # It's used to covert all the letter of a string to upper case
print(mystr2.replace("World","Earth")) # It's used replace any word to another