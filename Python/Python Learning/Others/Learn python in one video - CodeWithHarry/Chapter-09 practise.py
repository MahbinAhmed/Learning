# Chapter-09 practise
# Q1
# f = open("Poem.txt","r")
# a = f.read()
# if "Twinkle" in a:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()

# Q2
# def hs():
#     return 60
# hiscore = hs()
# with open("Score.txt","r") as f:
#     score=int(f.read())
#
# if score< hiscore:
#     with open("Score.txt","w")as f:
#         uhs=(f.write(str(hiscore)))

# Q3
# Q4
# with open("Poem.txt","r")as f:
#     content= f.read()
#
# content = content.replace("Fwinkle", "Twinkle")
#
# with open("Poem.txt","w")as f:
#     f.write(content)

# Q8
# with open("Text.txt","r")as f:
#     content = f.read()
#
# with open("Copy.txt","w")as f:
#     f.write(content)

# Q9
# file1 = "Text.txt"
# file2 = "Copy.txt"
# with open("Text.txt")as f:
#     f1= f.read()
# with open("Copy.txt")as f:
#     f2= f.read()
#
# if f1 == f2:
#     print("Both files are same")
# else:
#     print("Both files are not same")

# Q10
with open("Poem.txt","w")as f:
    f.write("")