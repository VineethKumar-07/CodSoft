import tkinter as tk
import random

def getComputerChoice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determineWinner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return "Draw"
    elif (playerChoice == "Rock" and computerChoice == "Scissors") or (playerChoice == "Paper" and computerChoice == "Rock") or (playerChoice == "Scissors" and computerChoice == "Paper"):
        return "Player wins!"
    else:
        return "Computer wins!"

def play(choice):
    if choice:
        computerChoice = getComputerChoice()
        result = determineWinner(choice, computerChoice)
        resultLabel["text"] = result
        playerLabel["text"] = f"Player: {choice}"
        computerLabel["text"] = f"Computer: {computerChoice}"

root = tk.Tk()
root.title("Rock Paper Scissors Game")

buttonFont = ("Arial", 16, "bold")
label_font = ("Arial", 14, "normal")

rockButton = tk.Button(root, text="Rock", command=lambda: play("Rock"), font=buttonFont)
paperButton = tk.Button(root, text="Paper", command=lambda: play("Paper"), font=buttonFont)
scissorsButton = tk.Button(root, text="Scissors", command=lambda: play("Scissors"), font=buttonFont)

playerLabel = tk.Label(root, text="Player", font=label_font)
computerLabel = tk.Label(root, text="Computer", font=label_font)
resultLabel = tk.Label(root, text="", font=label_font)

rockButton.grid(row=0, column=0, padx=10, pady=10)
paperButton.grid(row=0, column=1, padx=10, pady=10)
scissorsButton.grid(row=0, column=2, padx=10, pady=10)
playerLabel.grid(row=1, column=0)
computerLabel.grid(row=1, column=2)
resultLabel.grid(row=2, column=1)

resetButton = tk.Button(root, text="Reset", command=lambda: play(""), font=buttonFont)
resetButton.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
