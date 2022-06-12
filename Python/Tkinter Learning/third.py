from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("900x600")

pphoto = PhotoImage(file="1.png")

# For JPG
images = Image.open("1.jpg")
photo = ImageTk.PhotoImage(images)

labeler = Label(image=photo,)
labeler.pack()
labeler2 = Label(image=pphoto)
labeler2.pack()

root.mainloop()