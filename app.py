import random

# Goal is to develop the logic of the Python minigame with the help of GitHub Copilot based in the specifications bellow.

#   Specification
# As we learned in the introduction to this challenge, the winner of the game is determined by three simple rules:

# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.


#   What you should consider in the game interactions
#   The computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. 
#   Your interaction in the game will be through the console (Terminal).

#   The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#   At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#   By the end of each round, the player can choose whether to play again.
#   Display the player's score at the end of the game.
#   The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.


#   The game logic:
#   The game should be able to handle the following scenarios:

#   Player wins:
#   Player chooses rock and the computer chooses scissors.
#   Player chooses scissors and the computer chooses paper.
#   Player chooses paper and the computer chooses rock.

#   Player loses:
#   Player chooses rock and the computer chooses paper.
#   Player chooses scissors and the computer chooses rock.
#   Player chooses paper and the computer chooses scissors.

#   Tie:
#   Player chooses rock and the computer chooses rock.
#   Player chooses scissors and the computer chooses scissors.
#   Player chooses paper and the computer chooses paper.

#   The game should be able to handle invalid inputs, such as numbers or other words that are not in the list of options (rock, paper, or scissors).
#   The game should be able to handle the player's choice to play again or not at the end of each round.
#   The game should display the player's score at the end of the game.


def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)

        print(f"Player chooses {player_choice}.")
        print(f"Computer chooses {computer_choice}.")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("Player wins!")
            player_score += 1
        else:
            print("Player loses!")
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()












