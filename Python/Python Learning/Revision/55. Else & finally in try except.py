# Else & finally in try except

try:
    print("alsdfj")

except Exception as e:
    print(e)

else:
    print("Printed without except block")

finally:
    print("This line will be print with both try and except blocks")