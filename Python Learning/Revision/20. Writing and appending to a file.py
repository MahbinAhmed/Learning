# Writing

# f = open("Writing&Appending.txt","w")
# f.write("This line is written using python.")
# f.close()

# Appending
# f = open("Writing&Appending.txt","a")
# f.write("\nThis line is written usinng append method of python")
# f.close()

# Read & Write both
f = open("Writing&Appending.txt","r+")
print(f.read())
f.close()