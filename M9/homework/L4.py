import tkinter as tk
import os


root = tk.Tk()
root.title("File Handling App")
root.geometry("400x400")


tk.Label(root, text="File Name", font=("Arial", 12)).pack(pady=5)
file_entry = tk.Entry(root, width=30)
file_entry.pack()


tk.Label(root, text="File Text", font=("Arial", 12)).pack(pady=5)
text_area = tk.Text(root, width=40, height=8)
text_area.pack()

result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)


def create_file():
    filename = file_entry.get()
    open(filename, "w")
    result_label.config(text="File Created Successfully ✅")


def write_file():
    filename = file_entry.get()
    content = text_area.get("1.0", tk.END)
    with open(filename, "w") as file:
        file.write(content)
    result_label.config(text="Data Written Successfully ✍️")


def read_file():
    filename = file_entry.get()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, data)
        result_label.config(text="File Read Successfully 📖")
    else:
        result_label.config(text="File Not Found ❌")


def delete_file():
    filename = file_entry.get()
    if os.path.exists(filename):
        os.remove(filename)
        text_area.delete("1.0", tk.END)
        result_label.config(text="File Deleted Successfully 🗑️")
    else:
        result_label.config(text="File Not Found ❌")


tk.Button(root, text="Create File", width=15, command=create_file).pack(pady=2)
tk.Button(root, text="Write File", width=15, command=write_file).pack(pady=2)
tk.Button(root, text="Read File", width=15, command=read_file).pack(pady=2)
tk.Button(root, text="Delete File", width=15, command=delete_file).pack(pady=2)

root.mainloop()
