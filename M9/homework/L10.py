import tkinter as tk
import random


win = tk.Tk()
win.title("Number Guess Game")
win.geometry("300x250")


secret = random.randint(1, 10)


tk.Label(win, text="Guess the Number (1 - 10)",
         font=("Arial", 14, "bold")).pack(pady=10)


guess_entry = tk.Entry(win)
guess_entry.pack(pady=5)


result = tk.Label(win, text="")
result.pack(pady=10)

def check():
    guess = int(guess_entry.get())

    if guess == secret:
        result.config(text="Correct! You Win 🎉", fg="green")
    elif guess > secret:
        result.config(text="Too High 😯", fg="blue")
    else:
        result.config(text="Too Low 😐", fg="red")


tk.Button(win, text="Check Guess",
          command=check).pack(pady=10)


win.mainloop()
