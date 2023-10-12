import random

# Function to determine the winner for a single round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to display the choices and result
def display_result(user_choice, computer_choice, result):
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    print(result)

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"User Score: {user_score} | Computer Score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Main program
print("Welcome to Rock, Paper, Scissors!")
play_game()
