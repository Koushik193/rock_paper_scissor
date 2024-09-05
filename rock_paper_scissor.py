import random

def display_welcome_message():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    print("Enter your choice (rock, paper, scissors) and see who wins!")

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_results(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("The computer wins!")

def main():
    display_welcome_message()

    user_wins = 0
    computer_wins = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        winner = determine_winner(user_choice, computer_choice)
        display_results(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
        
        rounds += 1
        
        print(f"\nScore after {rounds} round(s):")
        print(f"You: {user_wins}")
        print(f"Computer: {computer_wins}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThanks for playing!")
    print(f"Final Score:")
    print(f"You: {user_wins}")
    print(f"Computer: {computer_wins}")

if __name__ == "__main__":
    main()
