from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry('500x500')

upload = Image.open("img.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=450, width=450)

label.place(x=50, y=0)
label2 = Label(root, text="This is an image", font=("Arial", 20))
label2.place(x=50, y=420)

root.mainloop()