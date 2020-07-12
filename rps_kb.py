import random
# Write a program to play RPS with 1 user
# Rules:
    # r > s
    # s > p
    # p > r
wins = 0
losses = 0
ties = 0

# Flow
# Start up interactions
possible_choices = ["rock", "paper", "scissors"]
programs_choice = random.choice(possible_choices)
print(programs_choice)
# Users will specify their choice
users_choice = input("Choose rock, paper, or scissors")
# Computer makes a choice

# Both choices are made
# Compare choices and determine a winner
if users_choice == "rock":
    if programs_choice == "rock":
        print("You tied!")
        ties += 1
    elif programs_choice == "paper":
        # program wins
        print("You lose")
        losses += 1
# Keep track of scores
# Allow user to end game
