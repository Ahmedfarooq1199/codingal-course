import tkinter as tk
import random
import string


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")


tk.Label(root, text="Password Length", font=("Arial", 12)).pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)


def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    result_label.config(text=password)


tk.Button(root, text="Generate Password", command=generate_password).pack()

root.mainloop()
