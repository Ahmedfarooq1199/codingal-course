import tkinter as tk

window = tk.Tk()
window.configure(bg="pink")
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=5,
        )
        frame.grid(row=i, column=j, padx=3, pady=3)
        label = tk.Label(master=frame,text=f"Row {i}\nColumn {j}")
        label.pack()
window.mainloop()