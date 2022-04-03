import random

wins = 0
losses = 0 
ties = 0
choices = ['r', 'p', 's']

def compare(player_choice, comp_choice):
    if player_choice == comp_choice:
        return 0
    elif(player_choice == 'r' and comp_choice == "s") or \
        (player_choice == 'p' and comp_choice == 'r' ) or \
        (player_choice == 's' and comp_choice == 'p'):
        return 1
    else:
        return -1

while True:
    print(f'Score: {wins} - {losses} - {ties}')
    cmd = input("Choose r, p, or s: ")
    ai_choice = choices[random.randrange(3)]
    print(f'Computer chose {ai_choice}')
    results = compare(cmd, ai_choice)
    if results == 1:
        wins += 1
        print("You won!")
    elif results == -1:
        losses += 1
        print("Sorry You Lose")
    elif results == 0:
        ties += 1
        print("Tie!")
    if cmd == 'q':
        print("Goodbye")
        break
    