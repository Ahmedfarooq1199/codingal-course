import tkinter as tk

win = tk.Tk()
win.title("File Handling")
win.geometry("300x250")


box = tk.Text(win, height=8, width=30)
box.pack(pady=10)

def save():
    f = open("myfile.txt", "w")
    f.write(box.get("1.0", tk.END))
    f.close()

def read():
    f = open("myfile.txt", "r")
    box.delete("1.0", tk.END)
    box.insert(tk.END, f.read())
    f.close()


tk.Button(win, text="Save", width=10, command=save).pack(pady=5)
tk.Button(win, text="Read", width=10, command=read).pack(pady=5)

win.mainloop()
