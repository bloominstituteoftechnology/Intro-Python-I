# Things that could be improved:

# Make way the computer pick a choice smarter so that it
# wins more consistently

# Allow more choices other than rock, paper or scissors

# Save the outcomes

# Sanitize the user input: make it so that program can handle
# shorthand, like "r" for rock

# Be smarter about comparing user and computer choices

# Add some funny banter / commentary from the computer

# Add more game types (best of 3)

# Win/loss percentage

# Encapsulate the comparison logic in its own function to make the more DRY

wins = 0
losses = 0
ties = 0

choices = ["rock", "paper", "scissors"]

# Takes input both the player's and computer's choices
# decides the outcome
# have it return 0 to indicate tie, 1 to indicate user won, and
# -1 to indicate computer won


def compare_choices(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    # player wins
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return 1
    # player loses
    else:
        return -1


# Keep all this in loop until user quits
while True:
    users_choice = input("Choose rock, paper or scissors (or quit): ")

    if users_choice == "quit":
        print("see you next time!")
        print("-----" * 5)
        break

    elif users_choice not in choices:
        print("I don't understand that choice")
        print("-----" * 5)
        continue

    print("User choice:", users_choice)

    import random

    prog_choice = random.choice(choices)
    print("Program Choice:", prog_choice)

    # Refactored to make it more easily readable
    result = compare_choices(users_choice, prog_choice)
    if result == 0:
        print("A tie!")
        ties += 1
    elif result == 1:
        print("You won!")
        wins += 1
    else:
        print("Computer won!")
        losses += 1

    print(f"Wins: {wins}, ties: {ties}, losses: {losses}")
    print("-----" * 5)
