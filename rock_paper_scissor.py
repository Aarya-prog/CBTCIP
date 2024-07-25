import random

# Function to get the user's choice
def get_user_choice():
    while True:
        try:
            user_input = input("Enter a choice (rock[1], paper[2], scissors[3]): ")
            user_action = int(user_input)
            if user_action in choices:
                return choices[user_action]
            else:
                print("Invalid choice! Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return f"{user_choice.capitalize()} beats {computer_choice}! You win!"
    else:
        return f"{computer_choice.capitalize()} beats {user_choice}! You lose."

# Main game loop
while True:
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    
    # Explain the rules to the user
    print("Welcome to the Rock-Paper-Scissors game!")
    print("Rules: \n"
          "1. Rock beats Scissors\n"
          "2. Paper beats Rock\n"
          "3. Scissors beat Paper\n"
          "To play, enter the number corresponding to your choice:\n"
          "1 for Rock, 2 for Paper, 3 for Scissors\n")
    
    # Get the user's choice
    user_choice = get_user_choice()
    
    # Generate the computer's choice
    computer_choice = random.choice(list(choices.values()))
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    
    # Determine and display the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    # Ask the user if they want to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye!")
        break
