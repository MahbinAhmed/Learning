import os

# print(os.getcwd())
# print(os.listdir())
# os.chdir("G:\\")
# print(os.getcwd())
# print(os.listdir())
# print(os.mkdir("Tempor"))
# print(os.makedirs("Tempor/ary"))
# os.rename("Tempor","Temporary")
# print(os.path.join("G:/","//nothing.txt"))
# print(os.path.exists("G://"))
# print(os.path.isfile("G://Learning"))
# os.mkdir("sample.txt")
# os.rmdir("sample.txt")
# Next lines are used to delete an empty file and a non empty file
# cwd = os.getcwd()
# path1 = os.path.join(cwd,"Temporary")
# os.chdir(path1)
# print(os.getcwd())
# os.chdir()
# os.rmdir("ary")
# os.rmdir("Temporary") #It deletes only empty files

# f = open("sample.txt","w")
# os.remove("Sample.txt")
# print(os.name)
# print(os.error)
# a = os.popen("hello.json","w") #It is similar to file open
# a.write("Hello guys")
# print(a)
# os.close(a)

# print(os.path.getsize("Regex.py"))

set1 = {"Yellow","Orange","Black"}
set2 = {"Orange","Blue","Pink"}
set3 = set1.difference(set2)
print(set3)