from tkinter import *

window =Tk()
window.title('tkinter Sample Window')
window.geometry('300x300')

greeting= Label(text="Hello User", fg='black', bg='White')

button = Button(text='Click Me', fg='black', bg='White')

entry = Entry(fg="yellow", bg="blue", width=100)

greeting.pack()
button.pack()   
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=10)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox =Text(fg='green', bg='white')
textbox.pack()

window.mainloop()
