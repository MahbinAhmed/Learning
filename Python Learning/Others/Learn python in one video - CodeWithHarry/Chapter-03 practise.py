# Chapter-03 practise

# Q1
name=input("Enter your name here:\n")
print("Good morning, ", name)

# Q2
bw = '''Hello <name>,
Happy birthday, many many happy returns of the day.
Date=<date>'''
bbn= input("Enter your name here\n")
bd= input("Enter your Birthday date\n")
bw=bw.replace("<name>",bbn)
bw=bw.replace("<date>",bd)
print(bw)

# Q3
st="It is a string with double    spaces"
doublespaces= st.find("  ")
print(doublespaces)

# Q4
ts ="It is a string with double  spaces"
ts= ts.replace("  ", " ")
print(ts)