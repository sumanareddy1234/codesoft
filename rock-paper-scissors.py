import random

# Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the result
def display_result(user_choice, computer_choice, winner):
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

# Main game loop
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        # Get user's choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        
        # Validate input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Get computer's choice
        computer_choice = get_computer_choice()
        
        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Display the result
        display_result(user_choice, computer_choice, winner)
        
        # Update the score
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        # Display the score
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
play_game()
