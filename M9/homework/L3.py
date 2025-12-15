import tkinter as tk
import time
import random


root = tk.Tk()
root.title("Python Robot")
root.geometry("400x350")


jokes = [
    "I love Python 🐍",
    "Why computer is fast? Because it eats RAM 😄",
    "I am learning like you 🤖"
]

def robot_reply():
    user = entry.get().lower()

    if user == "hello":
        reply = "Hello! I am your robot 🤖"

    elif user == "time":
        reply = "Time is " + time.strftime("%H:%M:%S")

    elif user == "joke":
        reply = random.choice(jokes)

    elif user == "bye":
        reply = "Goodbye! See you again 👋"

    else:
        reply = "I don't understand 😐"

    chat_label.config(text="🤖 Robot: " + reply)
    entry.delete(0, tk.END)


tk.Label(root, text="🤖 Python Robot", font=("Arial", 16, "bold")).pack(pady=10)


entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)


tk.Button(root, text="Send", command=robot_reply, width=15).pack(pady=5)


chat_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
chat_label.pack(pady=20)


tk.Label(
    root,
    text="Commands: hello | time | joke | bye",
    font=("Arial", 10)
).pack()

root.mainloop()
