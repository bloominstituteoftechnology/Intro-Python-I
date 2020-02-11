import random
# Create a rock paper scissors game in Python

# Player should be able to type r, p, or s
# Computer will pick r, p or s

# Game will print out the results and keep track of wins, losses and ties

# Type q to quit


# Build a REPL


choices = ["r", "p", "s"]
wins = 0
losses = 0
ties = 0

# Define a function that


def eval_moves(player_move, cpu_move):
    '''
    Evaluates player move and cpu move, returns results

    Player move and cpu move must be r/p/s
    '''
    winning_moves = {"r": "s", "s": "p", "p": "r"}
    if player_move == cpu_move:
        print("You tie")
        return 0
    elif winning_moves[player_move] == cpu_move:
        print("You win!")
        return 1
    else:
        print("You came close, try again!")
        return -1


# LOOP
while True:
    # READ
    # PRINT results and score
    print(f"\nWins: {wins}, Losses: {losses}, Ties: {ties}")
    cmd = input("~~> ")
    # EVAL
    # Computer picks r/p/s
    cpu_move = random.choice(choices)
    print(f"CPU picks {cpu_move}")
    # Compare player command to cpu command
    if cmd in choices:
        results = eval_moves(cmd, cpu_move)
        if results == 0:
            ties += 1
        elif results == 1:
            wins += 1
        else:
            losses += 1
    elif cmd == "q":
        print("Goodbye!")
        break
    else:
        print("I did not understand that command. Please pick r, p, s, or q.")
    # Update results based on win/loss/tie
