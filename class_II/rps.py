# PLANNING:

# Write a program to play Rock Paper Scissors with a user
# Let's flesh out the rules and think about how this is going
# to work

# UNDERSTANDING:
### Rules: Rock > Scissors
#        Scissors > Paper
#        Paper > Rock

# PLANNING:
# Flow:
# Start up program

wins = 0
losses = 0
ties = 0

# Keep all this in loop until user quits

while True:
    # User will specify their choice (rock, paper or scissors)
    # or can type "quit" to exit program

    # How does the program read the user's choice?
    # Use Python's `input()`` function
    users_choice = input("Choose rock, paper or scissors (or quit): ")

    if users_choice == "quit":
        print("see you next time!")
        print("-----" * 5)
        break

    print("User choice:", users_choice)

    # Program also needs to specify its choice
    # How does the program determine its choice?
    # Just have it randomly pick a choice
    # How do we have the program make a random choice?
    # Use Python's `random.choice()` function
    import random

    choices = ["rock", "paper", "scissors"]
    prog_choice = random.choice(choices)
    print("Program Choice:", prog_choice)

    # Once both choices are made, compare them via the rules to
    # see who won
    # How do we do the comparison?
    # Use if statements
    # Keep track of number of wins, losses and ties for the user
    # How do we keep track of these things?
    # Have seperate variables for each

    if users_choice == "rock":
        if prog_choice == "rock":
            print("A tie!")
            ties += 1
        elif prog_choice == "paper":
            print("Program won!")
            losses += 1
        else:
            print("You won!")
            wins += 1
    elif users_choice == "paper":
        if prog_choice == "rock":
            print("You won!")
            wins += 1
        elif prog_choice == "paper":
            print("A tie!")
            ties += 1
        else:
            print("Program won!")
            losses += 1
    elif users_choice == "scissors":
        if prog_choice == "rock":
            print("Program won!")
            losses += 1
        elif prog_choice == "paper":
            print("You won!")
            wins += 1
        else:
            print("A tie!")
            ties += 1
    else:
        print("I don't understand that choice")
        print("-----" * 5)
        # go on to next iteration of game loop
        continue

    print(f"Wins: {wins}, ties: {ties}, losses: {losses}")
    print("-----" * 5)
