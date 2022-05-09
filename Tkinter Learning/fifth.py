from tkinter import *

root = Tk()
root.geometry("900x600")

f1 = Frame(root,bg="Black",borderwidth=6)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root,bg="grey",borderwidth=50)
f2.pack(side=TOP,fill=X)

label1 = Label(f1,text="Hello World")
label1.pack(pady=150)

label2 = Label(f2, text="This is menubar")
label2.pack()

root.mainloop()