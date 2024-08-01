import tkinter as tk
from random import choice
from itertools import cycle

# Initialize the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("600x400")

# Unicode icons for rock, paper, and scissors
rock_icon = "✊"
paper_icon = "✋"
scissors_icon = "✌️"

# Dictionary to map choices to icons
icons = {
    "Rock": rock_icon,
    "Paper": paper_icon,
    "Scissors": scissors_icon
}

# Function to determine the winner
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    animate_result(user_choice, computer_choice, result)

# Function to animate the result
def animate_result(user_choice, computer_choice, result):
    icons_cycle = cycle([rock_icon, paper_icon, scissors_icon])
    steps = 10  # Number of frames in the animation
    delay = 100  # Delay between frames in milliseconds

    def update_animation(step=0):
        if step < steps:
            user_choice_label.config(text=next(icons_cycle))
            computer_choice_label.config(text=next(icons_cycle))
            window.after(delay, update_animation, step + 1)
        else:
            user_choice_label.config(text=icons[user_choice])
            computer_choice_label.config(text=icons[computer_choice])
            result_label.config(text=f"Computer chose: {icons[computer_choice]}\n{result}")

    update_animation()

# Set up the interface elements
tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

frame = tk.Frame(window)
frame.pack(pady=20)

rock_button = tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(window, text=rock_icon, font=("Arial", 50))
user_choice_label.pack(side=tk.LEFT, padx=50)

computer_choice_label = tk.Label(window, text=rock_icon, font=("Arial", 50))
computer_choice_label.pack(side=tk.RIGHT, padx=50)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Start the main event loop
window.mainloop()
