from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
     messagebox.showwarning("Alert", "Stop! virus detected")


button = Button(root, text="Click Me", command=msg)
button.place(x=50,y=80)
root.mainloop()