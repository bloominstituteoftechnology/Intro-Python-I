import random


def show_welcome_message():
    welcome_message = "Welcome to Rock, Paper, Scissors!"
    print(welcome_message)


def get_historical_data():
    text_file = open("history.txt", "r")
    text_data = text_file.read().split(",")
    text_file.close()
    return {"wins": int(text_data[0]),
            "ties": int(text_data[1]),
            "losses": int(text_data[2])
            }


def show_historical_data_message():
    print(historical_data_message %
          (score["wins"], score["ties"], score["losses"]))


def get_user_choice():
    choice = input("Choose one: [1] rock, [2] paper, [3] scissors, [9] quit\n")
    while choice.isalpha() or int(choice) not in choice_options.keys():
        print('Invalid selection. Try again.')
        choice = input(
            "Choose one: [1] rock, [2] paper, [3] scissors, [9] quit\n")

    return choice_options[int(choice)]


def quit_game(wins, ties, losses):
    text_file = open("history.txt", "w")
    text_file.write(str(wins) + "," + str(ties) + "," + str(losses))
    text_file.close()


def compare_choices_and_get_result(user, computer):
    print(
        f'\nYou picked {choice_emojis[user]}  {user} , and the computer picked {choice_emojis[computer]}  {computer}.')
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "loss"


def display_result_message_and_update_score(result):
    if result == "tie":
        print(tie_message)
        score["ties"] += 1
    elif result == "win":
        print(win_message)
        score["wins"] += 1
    else:
        print(loss_message)
        score["losses"] += 1


score = {"wins": 0,
         "ties": 0,
         "losses": 0
         }

welcome_message = "Welcome to Rock, Paper, Scissors!"
historical_data_message = "Wins: % s, Ties: % s, Losses: % s"
quit_message = "Thanks for playing Rock, Paper, Scissors!"
win_message = "Congratulations, you won!"
loss_message = "Sorry, you lost!"
tie_message = "It was a tie."

historical_data = get_historical_data()
score["wins"] = historical_data["wins"]
score["ties"] = historical_data["ties"]
score["losses"] = historical_data["losses"]

choice_options = {
    1: "rock",
    2: "paper",
    3: "scissors",
    9: "quit"
}

choice_emojis = {
    "paper": "🧻",
    "rock": "⛰️",
    "scissors": "✂️"
}

# Start of Game
show_welcome_message()
show_historical_data_message()

# First user choice
user_choice = get_user_choice()

# Game Loop
while user_choice != "quit":
    computer_choice = choice_options[random.randint(1, 3)]
    result = compare_choices_and_get_result(user_choice, computer_choice)
    display_result_message_and_update_score(result)
    show_historical_data_message()
    print('\n')
    user_choice = get_user_choice()

# Quit game if user exits game loop
quit_game(score["wins"], score["ties"], score["losses"])
