#!/usr/bin/env python3
import random
# Create Rock Paper Scissors Game in Python

# Player should be able to type r, p, or s
# Computer will pick r, p, or s

# Game will print out the results and keep track of wins, losses, and ties

# Type q to quit


# Build REPL


wins = 0
losses = 0
ties = 0

choices = ["r", "p", "s"]

loss_string = "Close, but no cigar!"
win_string = "You won! Nice work!"
tie_string = "You tied. Try again!"

def eval_moves(player_move, cpu_move):
    '''
    Evaluates player move & CPU move, then returns results
    Player move & CPU move must be either r/p/s
    '''
    
    # Key is the player move. Value is the cpu's losing move that results in a win for the player.
    winning_moves = {"r": "s", "p": "r", "s": "p"}
    if player_move == cpu_move:
        print(tie_string)
        return 0
    elif winning_moves[player_move] == cpu_move:
        print(win_string)
        return 1
    else:
        print(loss_string)
        return -1

# Loop
while True:
	# READ
	print(f"\nWins: {wins}, Losses: {losses}, Ties: {ties}")
	cmd = input("~~>")
	
	#EVAL
	# Computer Picks r/p/s
	cpu_move = random.choice(choices)
	print(f"CPU picks {cpu_move}")
	
	# Compare player command to cpu command
	if cmd in choices:
		results = eval_moves(cmd, cpu_move)
		if results == 0:
			ties += 0
		elif results == 1:
			wins += 1
		else:
			losses += 1
	elif cmd == "q":
		print("Goodbye!")
		break
	else:
		print("I did not recognize input as a valid command. Please pick r, p, s, or q.")
		# Update results based on win/loss/tie
    
