import random

choices = ['r', 'p', 's']
name = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
rock = {'r': 'Tie', 'p': 'Lose', 's': 'Win'}
paper = {'r': 'Win', 'p': 'Tie', 's': 'Lose'}
scissors = {'r': 'Lose', 'p': 'Win', 's': 'Tie'}
checker = {'r': rock, 'p': paper, 's': scissors}
scorer = {'Win': 0, 'Lose': 0, 'Tie': 0}


def check(inp):
    diction = checker[inp]
    return diction


print('Welcome to Rock Paper Scissors!')
while True:
    program_choice = random.choice(choices)

    inp = input('Please choose (r)ock, (p)aper, or (s)cissors or (q) to quit\n')

    while inp.lower() not in choices and inp.lower() != 'q':
        inp = input('Please choose (r)ock, (p)aper, or (s)cissors, or (q) to quit\n')

    if inp.lower() == 'q':
        print('Goodbye!')
        print(
            f"Final Record:\nWins: {scorer['Win']} Losses: {scorer['Lose']} Ties: {scorer['Tie']}")
        break

    else:
        dict_to_use = check(inp)
        print(
            f'Program Choice: {name[program_choice]}\nYour Choice: {name[inp]}')
        print(dict_to_use[program_choice])
        scorer[dict_to_use[program_choice]] += 1
        print(
            f"Wins: {scorer['Win']} Losses: {scorer['Lose']} Ties: {scorer['Tie']}")
