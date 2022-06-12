# Chapter-03(Strings,)
#Strings
a = "Hello world"
print(a)
print(type(a))

Name= "Mahid"
Greeting= "Good morning, "
b = Greeting+Name
print(b)

print(Name[1])
print(Name[1:3])
print(Name[-4:-1])
print(Name[::2])

# String functions
story = "a quick brown fox jumps over the lazy dogs"
print(len(story))
print(story.endswith("s"))
print(story.count("a"))
print(story.find("quick"))
print(story.capitalize())
print(story.replace("fox","cheetah"))

# Escape sequences
doc = "My name is Mahid. \n I read in \t class \\8"
print(doc)