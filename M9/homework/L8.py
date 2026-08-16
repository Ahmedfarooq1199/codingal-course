import tkinter as tk


win = tk.Tk()
win.title("Polygon Calculator")
win.geometry("300x250")


tk.Label(win, text="Polygon Perimeter", font=("Arial", 14, "bold")).pack(pady=10)


tk.Label(win, text="Number of sides:").pack()
sides_entry = tk.Entry(win)
sides_entry.pack()

tk.Label(win, text="Length of one side:").pack()
length_entry = tk.Entry(win)
length_entry.pack()


result = tk.Label(win, text="Perimeter = ")
result.pack(pady=10)


def calculate():
    sides = int(sides_entry.get())
    length = float(length_entry.get())
    perimeter = sides * length
    result.config(text="Perimeter = " + str(perimeter))


tk.Button(win, text="Calculate", command=calculate).pack(pady=10)


win.mainloop()
