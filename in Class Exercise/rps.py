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
    elif cmd == "r":
        if cpu_cmd == "r":
            print("You tie")
            ties += 1
        elif cpu_cmd == "p":
            print("You lose...")
            losses += 1
        elif cpu_cmd == "s":
            print("You win!")
            wins += 1
    elif cmd == "p":
        if cpu_cmd == "p":
            print("You tie")
            ties += 1
        elif cpu_cmd == "s":
            print("You lose...")
            losses += 1
        elif cpu_cmd == "r":
            print("You win!")
            wins += 1
    elif cmd == "s":
        if cpu_cmd == "s":
            print("You tie")
            ties += 1
        elif cpu_cmd == "r":
            print("You lose...")
            losses += 1
        elif cpu_cmd == "p":
            print("You win!")
            wins += 1
    else:
        print("I did not understand that command")








