''' This is a version of rock, paper, scissors taken from the televison series,
    The Big Bang Theory (S2E8).
    This version is called rock, paper, scissor, lizard spock.
    
There will be 2 players:
    - One player will be a human user.
    - The second player will a computer player that the human user is competing against.
Each player has 5 choices:
    - rock
    - paper
    - scissors
    - lizard 
    - spock 
There are three results after both the human and the computer make one of their choices:
    - win
    - lose
    - tie

    Rules: 
    
    1. Scissor cuts Paper
    2. Paper covers Rock
    3. Rock crushed Lizard
    4. Lizard poisons Spock
    5. Spock smashes scissors
    6. Scissors decapitates Lizard
    7. Lizzard eats Paper
    8. Paper disproves Spock
    9. Spock vaporizes Rock
    10. Rock crushes Scissors
        
    '''

import random

score = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

welcome_message = "Welcome to Rock, Paper, Scissors, Lizard, Spock!!!"
historical_data_message = "Wins: %s, Losses: %sTies: %s"
quit_message = "Thanks for playing! Come back soon for all of you decision making needs."
win_message = "Winner, Winner Chicken Dinner"
loss_message = "Wah Wah Wah Waaaaah... Sorry dude you lose."
tie_message = "Congratulations! You are as smart as a random choice generator!"

choice_options = {
    1: "rock",
    2: "paper",
    3: "Scissors",
    4: "lizard",
    5: "Spock",
    9: "Quit"
}


possible_choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
computer_choice = random.choice(possible_choices)

# Display Welcome Message
def show_welcome_message():
    welcome_message = 'Welcome to Rock, Paper, Scissors, Lizard Spock!'
    print(welcome_message)

# Load historical_data and populate variables with data
def get_historical_data():
    text_file = open('history.txt', 'r')
    text_data = text_file.read().split(',')
    text_file.close()
    return {
        'wins': int(text_data[0]),
        'losses': int(text_data[1]),
        'ties': int(text_data[2])
    }

# Display historical data message with historical data
def show_historical_data_message():
    print(historical_data_message %
          (score['wins'], score['losses'], score['ties']))

# Prompt user to make a choice between rock, paper, scissors, or quit
def get_user_choice():
    choice = input("[1] rock   [2] paper   [3] scissors [4] lizard [5] Spock  [9] quit\n")
    return choice_options[int(choice)]

# If quit, update text file with current wins, ties, losses data and exit game
def quit_game(wins, ties, losses):
    text_file = open('history.txt', 'w')
    text_file.write(str(wins) + ',' + str(ties) + ',' + str(losses))
    text_file.close()

# Compare user choice and computer choice
def compare_choices_and_get_result(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        return 'win'
    elif (user == 'rock' and computer == 'lizard') or (user == 'lizard' and computer == 'spock') or (user == 'spock' and computer == 'scissors'):
        return 'win' 
    elif (user == 'scissors' and computer == 'lizard ') or (user == 'lizard' and computer == 'paper') or (user == 'paper' and computer == 'spock'):
        return 'win'
    elif (user == 'spock' and computer == 'rock'):
         return 'win'
    else:
        return 'loss'

# Display message based on result of comparison
# Update wins, ties, and losses
def display_result_message_and_update_score(result):

    if result == 'win':
        print(win_message)
        score['wins'] += 1
    elif result == 'loss':
        print(loss_message)
        score['losses'] += 1
            
    else:
        print(tie_message)
        score['ties'] += 1
    
        
