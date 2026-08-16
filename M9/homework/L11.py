import tkinter as tk
import random

class GuessGame:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Number Guess Game")
        self.win.geometry("300x250")

        
        self.secret = random.randint(1, 10)

        
        tk.Label(
            self.win,
            text="Guess the Number (1 - 10)",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        
        self.entry = tk.Entry(self.win)
        self.entry.pack(pady=5)

        
        self.result = tk.Label(self.win, text="")
        self.result.pack(pady=10)

        
        tk.Button(
            self.win,
            text="Check Guess",
            command=self.check_guess
        ).pack(pady=10)

        self.win.mainloop()

    def check_guess(self):
        guess = int(self.entry.get())

        if guess == self.secret:
            self.result.config(text="Correct! You Win 🎉", fg="green")
        elif guess > self.secret:
            self.result.config(text="Too High 😯", fg="blue")
        else:
            self.result.config(text="Too Low 😐", fg="red")


GuessGame()
