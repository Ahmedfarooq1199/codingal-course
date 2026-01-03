import tkinter as tk
import random


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x450")
root.resizable(False, False)
root.config(bg="#1e272e")  # Dark background

choices = ["Rock", "Paper", "Scissors"]


title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 18, "bold"),
    fg="#fbc531",
    bg="#1e272e"
)
title_label.pack(pady=15)


user_label = tk.Label(
    root,
    text="Your Choice: ",
    font=("Arial", 12),
    fg="white",
    bg="#1e272e"
)
user_label.pack(pady=5)

computer_label = tk.Label(
    root,
    text="Computer Choice: ",
    font=("Arial", 12),
    fg="white",
    bg="#1e272e"
)
computer_label.pack(pady=5)

result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 16, "bold"),
    fg="#00cec9",
    bg="#1e272e"
)
result_label.pack(pady=25)


def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text="Your Choice: " + user_choice)
    computer_label.config(text="Computer Choice: " + computer_choice)

    if user_choice == computer_choice:
        result_label.config(text="Result: DRAW 😐", fg="#f1c40f")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="Result: YOU WIN 🎉", fg="#2ecc71")
    else:
        result_label.config(text="Result: YOU LOSE 😢", fg="#e74c3c")


btn_frame = tk.Frame(root, bg="#1e272e")
btn_frame.pack(pady=20)

rock_btn = tk.Button(
    btn_frame,
    text="🪨 Rock",
    width=15,
    font=("Arial", 11, "bold"),
    bg="#e84393",
    fg="white",
    activebackground="#fd79a8",
    command=lambda: play("Rock")
)
rock_btn.pack(pady=6)

paper_btn = tk.Button(
    btn_frame,
    text="📄 Paper",
    width=15,
    font=("Arial", 11, "bold"),
    bg="#0984e3",
    fg="white",
    activebackground="#74b9ff",
    command=lambda: play("Paper")
)
paper_btn.pack(pady=6)

scissors_btn = tk.Button(
    btn_frame,
    text="✂ Scissors",
    width=15,
    font=("Arial", 11, "bold"),
    bg="#00b894",
    fg="white",
    activebackground="#55efc4",
    command=lambda: play("Scissors")
)
scissors_btn.pack(pady=6)


footer = tk.Label(
    root,
    text="Made with Python Tkinter ❤️",
    font=("Arial", 9),
    fg="#b2bec3",
    bg="#1e272e"
)
footer.pack(side="bottom", pady=10)


root.mainloop()
