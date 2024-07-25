# Mastermind Game using Python

import time

class MastermindGame:
    def __init__(self):
        # Initialize game attributes
        self.player1_name = ""
        self.player2_name = ""
        self.player1_number = ""
        self.player2_number = ""
        self.guesses = {1: [], 2: []}  # Stores guesses for both players
    
    def set_player_names(self):
        # Set the names of the players
        self.player1_name = input("Enter Player 1's name: ")
        self.player2_name = input("Enter Player 2's name: ")

    def set_number(self, player):
        # Set the number to guess 
        if player == 1:
            self.player1_number = input(f"{self.player1_name}, set your 4-digit number: ")
        elif player == 2:
            self.player2_number = input(f"{self.player2_name}, set your 4-digit number: ")

    def guess_number(self, player):
        # Player guesses the opponent's number
        if player == 1:
            guess = input(f"{self.player1_name}, guess the number: ")
            self.guesses[1].append(guess)
        elif player == 2:
            guess = input(f"{self.player2_name}, guess the number: ")
            self.guesses[2].append(guess)
        return guess

    def check_guess(self, guess, actual_number):
        # Check the player's guess against the actual number
        correct_positions = ["X"] * len(actual_number)  # Holds correct digits in correct positions
        correct_digits_wrong_positions = []  # Holds correct digits in wrong positions
        used_indices = []  # Tracks indices of correct positions to avoid duplication

        # Check for correct digits in correct positions
        for i in range(len(guess)):
            if guess[i] == actual_number[i]:
                correct_positions[i] = guess[i]
                used_indices.append(i)
        
        # Check for correct digits in wrong positions
        for i in range(len(guess)):
            if guess[i] != actual_number[i] and guess[i] in actual_number:
                for j in range(len(actual_number)):
                    if actual_number[j] == guess[i] and j not in used_indices:
                        correct_digits_wrong_positions.append(guess[i])
                        used_indices.append(j)
                        break

        return correct_positions, correct_digits_wrong_positions

    def play_round(self):
        # Play a round of the game
        self.set_player_names()
        self.set_number(2)  # Player 2 sets the number first
        
        # Player 1 guessing Player 2's number
        while True:
            player1_guess = self.guess_number(1)
            correct_positions, correct_digits_wrong_positions = self.check_guess(player1_guess, self.player2_number)
            print(f"{self.player1_name} guessed {player1_guess}: positions correct: {''.join(correct_positions)}, digits correct but wrong positions: {correct_digits_wrong_positions}")
            if player1_guess == self.player2_number:
                print(f"{self.player1_name} guessed the number correctly !!")
                break
        
        player1_tries = len(self.guesses[1])
        print(f"{self.player1_name} took {player1_tries} tries to guess the number correctly.")
        if player1_tries == 1:
            print(f"{self.player1_name} wins and is crowned Mastermind!")
            return

        # A brief pause to simulate real game dynamics
        time.sleep(2)
        print(f"\nNow it's {self.player2_name}'s turn!\n")
        time.sleep(2)

        # Player 2 guessing Player 1's number
        self.set_number(1)  # Player 1 sets the number
        while True:
            player2_guess = self.guess_number(2)
            correct_positions, correct_digits_wrong_positions = self.check_guess(player2_guess, self.player1_number)
            print(f"{self.player2_name} guessed {player2_guess}: positions correct: {''.join(correct_positions)}, digits correct but wrong positions: {correct_digits_wrong_positions}")
            if player2_guess == self.player1_number:
                print(f"{self.player2_name} guessed the number correctly !!")
                break

        player2_tries = len(self.guesses[2])
        print(f"{self.player2_name} took {player2_tries} tries to guess the number correctly.")
        if player2_tries == 1:
            print(f"{self.player2_name} wins and is crowned Mastermind!")
            return

        # Determine the winner
        if player1_tries < player2_tries:
            print(f"{self.player1_name} wins and is crowned Mastermind!")
        elif player1_tries > player2_tries:
            print(f"{self.player2_name} wins and is crowned Mastermind!")
        else:
            print("It is a tie!")

# Run the game
game = MastermindGame()
game.play_round()
