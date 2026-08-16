import tkinter as tk
import math


win = tk.Tk()
win.title("Polygon Area Calculator")
win.geometry("320x280")

tk.Label(win, text="Polygon Area Calculator",
         font=("Arial", 14, "bold")).pack(pady=10)


tk.Label(win, text="Number of sides:").pack()
sides_entry = tk.Entry(win)
sides_entry.pack()


tk.Label(win, text="Length of one side:").pack()
length_entry = tk.Entry(win)
length_entry.pack()


result = tk.Label(win, text="Area = ")
result.pack(pady=15)


def calculate_area():
    n = int(sides_entry.get())
    s = float(length_entry.get())

    area = (n * s * s) / (4 * math.tan(math.pi / n))
    result.config(text="Area = " + str(round(area, 2)))


tk.Button(win, text="Calculate Area",
          command=calculate_area).pack(pady=10)


win.mainloop()
