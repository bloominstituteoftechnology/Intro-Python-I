import random

# Create a RPS game where player can type r, p or s, the computer chooses
# a random move, and the game tells you who won.

# You should be able to play multiple games and the game will tell you
# Your score after each round.

# Type q to quit.


# Create a REPL

wins = 0
losses = 0
ties = 0

choices = ['r', 'p', 's']


# Define a function that compares player and cpu moves
# and returns 1 for a win, 0 for tie, -1 for loss

def compare_moves(player_move, cpu_move):
    if player_move == cpu_move:
        print("You tie.")
        return 0
    elif player_move == "r" and cpu_move == "s" or \
         player_move == "p" and cpu_move == "r" or \
         player_move == "s" and cpu_move == "p":
        print("You win!")
        return 1
    else:
        print("You don't win...")
        return -1


# LOOP
while True:
    # PRINT
    print(f"Score: {wins} / {losses} / {ties}")
    # READ
    cmd = input("-> ")
    # EVAL
    cpu_cmd = random.choice(choices)
    print(f"CPU picks {cpu_cmd}")
    # If q, quit the loop
    if cmd == "q":
        print("Goodbye!")
        break
    elif cmd in choices:
        result = compare_moves(cmd, cpu_cmd)
        if result == 1:
            wins += 1
        elif result == 0:
            ties += 1
        else:
            losses += 1
    else:
        print("I did not understand that command")

