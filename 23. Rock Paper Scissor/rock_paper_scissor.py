# Day 23: A rock-paper-scissor game


import random

print("Welcome to Rock Paper Scissors game!")

# Define the valid options
options = ["rock", "paper", "scissors"]

# Get the user's choice
user_choice = input("Choose your weapon (rock, paper, scissors): ").lower()

# Validate the user's choice
if user_choice not in options:
    print("Invalid choice. Please choose from 'rock', 'paper', or 'scissors'.")
else:
    # Get the computer's choice
    computer_choice = random.choice(options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time!")
