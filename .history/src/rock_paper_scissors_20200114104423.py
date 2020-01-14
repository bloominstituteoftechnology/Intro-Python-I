

# REPL
wins = 0
losses = 0
ties = 0

# LOOP
while True:
    # READ
cmd = input("->")
cpu_move = random.choice(choices)
# EVAL
if cmd == "r":
    if cpu_move == "r":
        print("Tie!")
        ties += 1
    elif if cpu_move == "s":
            
        print("Lose :(")
        losses +=1
    elif if cpu_move == "s":
        pass
if cmd == "q":
    # Quit
    print("Goodbye!")
break
else:
    print("I do not recognize that command")
#  PRINT
