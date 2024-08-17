import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
        result_label.config(fg="#FFFFFF")  # White for tie
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper') or \
            (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
        result_label.config(fg="#2ECC71")  # Green for win
        global user_score
        user_score += 1
    else:
        result = "You lose!"
        result_label.config(fg="#E74C3C")  # Red for lose
        global computer_score
        computer_score += 1

    result_label.config(text=result)
    update_scores()


# Function to update the scores
def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")


# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    result_label.config(text="", fg="#FFFFFF")
    computer_choice_label.config(text="")


# Main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x500")
root.configure(bg="#34495E")  # Dark blue background

# Initialize scores
user_score = 0
computer_score = 0

# Labels and Buttons
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Arial', 16), fg="#ECF0F1", bg="#34495E").pack(pady=20)

tk.Button(root, text="Rock", command=lambda: determine_winner('Rock'), font=('Arial', 14), bg="#2980B9",
          fg="#000000").pack(pady=10)
tk.Button(root, text="Paper", command=lambda: determine_winner('Paper'), font=('Arial', 14), bg="#2980B9",
          fg="#000000").pack(pady=10)
tk.Button(root, text="Scissors", command=lambda: determine_winner('Scissors'), font=('Arial', 14), bg="#2980B9",
          fg="#000000").pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 16), fg="#FFFFFF", bg="#34495E")  # Default color is white
result_label.pack(pady=20)

computer_choice_label = tk.Label(root, text="", font=('Arial', 14), fg="#ECF0F1", bg="#34495E")
computer_choice_label.pack(pady=10)

user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=('Arial', 14), fg="#ECF0F1", bg="#34495E")
user_score_label.pack(pady=10)

computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=('Arial', 14), fg="#ECF0F1",
                                bg="#34495E")
computer_score_label.pack(pady=10)

tk.Button(root, text="Reset Game", command=reset_game, font=('Arial', 14), bg="#E67E22", fg="#000000").pack(pady=20)

# Run the application
root.mainloop()
