import random


wins = 0
ties = 0
losses = 0
print('Welcome to Rock, Paper, Scissors!')
print('Wins: %s, Ties: %s, Losses: %s ' % (wins, ties, losses))
print('Please choose to continue...')

# users
user = int(input('[1] Rock, [2] Paper, [3] Scissors, [9] Quit'))
computer = random.randint(1, 3)

while not user == 9:
    # user chooses rock
    if user == 1:
        if computer == 1:
            print("Computer chose rock...tie!")
            ties += 1
        elif computer == 2:
            print("Paper covers Rock. You loose!")
            losses += 1
        elif computer == 3:
            print("Rock crushes Scissors, you win!")
            wins += 1
    # user chooses paper
    if user == 2:
        if computer == 2:
            print("Computer chose paper...tie!")
            ties += 1
        elif computer == 3:
            print("Scissors cut paper, you lose!")
            losses += 1
        elif computer == 1:
            print("Paper covers rock, you win!")
    # user chooses scissors
    if user == 3:
        if computer == 3:
            print("Computer chose Scissors...tie!")
            ties += 1
        elif computer == 1:
            print("Rock crushes scissors, you lose!")
            losses += 1
        elif computer == 2:
            print("Scissors cut paper, you win!")
            wins += 1
    print('Wins: %s, Ties: %s, Losses: %s ' % (wins, ties, losses))
    print('Please choose to continue...')

    # users
    user = int(input('[1] Rock, [2] Paper, [3] Scissors, [9] Quit'))
    computer = random.randint(1, 3)
