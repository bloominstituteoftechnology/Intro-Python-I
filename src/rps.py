import random
​
choices = ['r', 'p', 's']
​
wins = 0
losses = 0
ties = 0
​
# Create a REPL loop to process commands
while True:  # Loop
    # Read
    cmd = input("-> ")
​
  # CPU will pick a random choice
  cpu_choice = random.choice(choices)
​
  # REPL should accept 'r', 'p', 's' commands
  # 'q' to quit
  # Eval
  print(f"CPU chooses {cpu_choice}")
   if cmd == "r":
        # If cpu picks s, you win
        if cpu_choice == "s":
            wins += 1
            print("You win!")
        # If cpu picks r, you tie
        elif cpu_choice == "r":
            ties += 1
            print("You tie.")
        # If cpu picks p, you lose
        elif cpu_choice == "p":
            losses += 1
            print("You lose...")
    elif cmd == "p":
        # If cpu picks r, you win
        if cpu_choice == "r":
            wins += 1
            print("You win!")
        # If cpu picks p, you tie
        elif cpu_choice == "p":
            ties += 1
            print("You tie.")
        # If cpu picks s, you lose
        elif cpu_choice == "s":
            losses += 1
            print("You lose...")
    elif cmd == "s":
        # If cpu picks p, you win
        if cpu_choice == "p":
            wins += 1
            print("You win!")
        # If cpu picks s, you tie
        elif cpu_choice == "s":
            ties += 1
            print("You tie.")
        # If cpu picks r, you lose
        elif cpu_choice == "r":
            losses += 1
            print("You lose...")
    elif cmd == "q":
        # Break out of the loop
        print("Goodbye!")
        break
​
  # Print out the score and loop
  print(f"{wins} / {losses} / {ties}")
