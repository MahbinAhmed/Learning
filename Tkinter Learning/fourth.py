from tkinter import *
import os

root = Tk()
root.geometry("1500x700")
root.title(f"Trial GUI | {os.path}")

# wiki_text = Label(text='''Python is a high-level, general-purpose programming language.
# Its design philosophy emphasizes code readability with the use of significant indentation.
# Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.[30]
# Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. 
# It is often described as a "batteries included" language due to its comprehensive standard library.Guido van Rossum began working on Python in the late 1980s 
# as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, 
# cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions.
# Python 2 was discontinued with version 2.7.18 in 2020.[34]''', 
# bg="green", fg="white",padx=5,pady=80,font="Bahnschrift 16", borderwidth=10, relief=SUNKEN)

wiki_text = Label(text='''Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.[30]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. 
It is often described as a "batteries included" language due to its comprehensive standard library.Guido van Rossum began working on Python in the late 1980s 
as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, 
cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions.
Python 2 was discontinued with version 2.7.18 in 2020.[34]''',bg="green",fg="white",padx=50,pady=40,font="Bahnschrift 10", borderwidth=50, relief=SUNKEN)

wiki_text.pack(side="right",fill="y")
root.mainloop()

# Important Label Options
# text = adds text
# bd = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

# Important Pack Options
# anchor = "ne"
# side = BOTTOM,TOP,LEFT,RIGHT
# fill
# padx
# pady