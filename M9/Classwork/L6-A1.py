from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='lightblue')
root.geometry('650x400')

upload = Image.open("img.jpg")
upload = upload.resize((300, 300))

image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User, Welcome to Denomination Counter",
               bg='lightblue')
label1.place(x=100, y=340)
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate denomination counter")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Click Me", command=msg, bg='brown', fg='white')
button1.place(x=260, y=360)

def topwin():
    top=Toplevel()
    top.title("Denomination Counter")
    top.configure(bg='lightgreen')
    top.geometry('600x350')

    label = Label(top, text="Enter the Amount", bg='lightgreen')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes of each denomination", bg='lightgreen')
    
    l1 = Label(top, text="2000", bg='lightgreen')
    l2 = Label(top, text="500", bg='lightgreen')
    l3 = Label(top, text="100", bg='lightgreen')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid amount")

    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')

    label.place(x=200, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()
root.mainloop()

