import tkinter as tk
import random


window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x350")


choices = ["Rock", "Paper", "Scissors"]


result_label = tk.Label(window, text="Choose one", font=("Arial", 14))
result_label.pack(pady=20)


def play(player_choice):
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "Draw 🤝"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win 🎉"
    else:
        result = "Computer Wins 😢"

    result_label.config(
        text=f"You: {player_choice}\nComputer: {computer_choice}\n\n{result}"
    )


tk.Button(window, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(window, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)


window.mainloop()
