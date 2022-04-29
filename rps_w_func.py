import random

# Create a rock/paper/scissors REPL loop
# Have a computer AI to play against us
# Keep track of the score
# Rules: r beats s, s beats p, p beats r
# 
wins = 0
losses = 0
ties = 0
choices = ['r', 'p', 's']

def compare_answers(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    elif (player_choice == "r" and computer_choice == "s") or  \
         (player_choice == "p" and computer_choice == "r") or  \
         (player_choice == "s" and computer_choice == "p"):
        return 1
    else:
        return -1

while True:
    print(f"Score: {wins} - {losses} - {ties}")
    cmd = input("\nChoose r/p/s: ")
    # AI picks a random choice from r/p/s
    ai_choice = choices[random.randrange(3)]
    print (f"Computer chose {ai_choice}")
    results = compare_answers(cmd, ai_choice)
    if results == 1:
        wins += 1
        print("You win!")
    elif results == -1:
        losses += 1
        print("You lose")
    elif results == 0:
        ties += 1
        print("You tie")
    if cmd == "q":
        print("Goodbye!")
        break
