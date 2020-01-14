import random
from typing import List

def process_choices(player_move: str, cpu_move: str) -> int:
    '''Assume that both moves are r, p, or s'''
    winning_cases: Dict[str, str] = {"r": "s", "p": "r", "s": "p"}
    if player_move == cpu_move:
        # tie
        print("Tie")
        return 0
    # If the player matches a winning case, the user wins
    elif winning_cases[player_move] == cpu_move:
        # win
        print("Win!")
        return 1
    else:
        # lose
        print("Lost!")
        return -1

# REPL
wins: int = 0
losses: int = 0
ties: int = 0

choices: List[str] = ["r", "p", "s"]

# Loop

while True:
    cmd = input("-> ")
    cmd = cmd.lower()
    cpu_move = random.choice(choices)
    print(F"CPU picks {cpu_move}")
    # EVAL
    if cmd in choices:
        results = process_choices(cmd, cpu_move)
        if results == 0:
            ties += 1
        elif results == 1:
            wins += 1
        else:
            losses += 1
    elif cmd == "q":
        #quit
        print("Goodbye!")
        break
    else:
        print("I did not recognize that command")
    print(F"Wins: {wins}, Losses: {losses}, Ties: {ties}")
