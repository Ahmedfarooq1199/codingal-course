import tkinter as tk


window = tk.Tk()
window.title("File Handling")
window.geometry("400x350")
window.config(bg="lightyellow")


title = tk.Label(
    window,
    text="File Handling with Tkinter",
    font=("Arial", 16, "bold"),
    bg="lightyellow"
)
title.pack(pady=10)


text_box = tk.Text(window, width=40, height=10)
text_box.pack(pady=10)


def save_file():
    file = open("data.txt", "w")
    file.write(text_box.get("1.0", tk.END))
    file.close()
    result_label.config(text="Data Saved Successfully", fg="green")


def open_file():
    file = open("data.txt", "r")
    content = file.read()
    file.close()

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, content)
    result_label.config(text="Data Loaded Successfully", fg="blue")


save_btn = tk.Button(
    window,
    text="Save to File",
    width=15,
    bg="lightgreen",
    command=save_file
)
save_btn.pack(pady=5)

open_btn = tk.Button(
    window,
    text="Open File",
    width=15,
    bg="lightblue",
    command=open_file
)
open_btn.pack(pady=5)

result_label = tk.Label(window, text="", bg="lightyellow", font=("Arial", 10))
result_label.pack(pady=10)


window.mainloop()
