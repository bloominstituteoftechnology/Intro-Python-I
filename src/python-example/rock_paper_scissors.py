#import module we need
import random

#file i/o functions for historical results
def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results( w, t, l):
    text_file = open("history.txt", "w")
    text_file.write( str(w) + "," + str(t) + "," + str(l))
    text_file.close()

#welcome message
results = load_results()
wins = int(results[0])
ties = int( results[1])
losses = int(results[2])
print("Welcome to Rock, Paper, Scissors!")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")


#initialize user, computer choices
computer = random.randint(1,3)
user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

#gamplay loop
while not user == 9:
    #user chooses ROCK
    if user == 1:
        if computer == 1:
            print("Computer chose rock...tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper...computer wins :(")
            losses += 1
        else:
            print("Computer chose scissors...you wins :)")
            wins += 1

    #user chooses PAPER
    elif user == 2:
        if computer == 1:
            print("Computer chose rock...you win :)")
            wins += 1
        elif computer == 2:
            print("Computer chose paper...tie!")
            ties += 1
        else:
            print("Computer chose scissors...computer wins :(")
            losses += 1
    
    #user chooses SCISSORS
    elif user == 3:
        if computer == 1:
            print("Computer chose rock...computer wins :(")
            losses += 1
        elif computer == 2:
            print("Computer chose paper...you win :)")
            wins += 1
        else:
            print("Computer chose scissors...tie!")
            ties += 1
    else:
        print("Invalid selection. Please try again.")
    #print updated stats
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    #prompt user to make another selection
    print("Please choose to continue...")
    #initialize user, computer choices
    computer = random.randint(1,3)
    user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

# #game over, save results
save_results(wins, ties, losses)









# ```import random


# class Player():
#     def __init__(self,name):
#         self.name = name
#         self.wins = 0
#         self.losses = 0
#         self.ties = 0
#     def __str__(self):
#         return f"\n{self.name}\n{self.wins} - {self.losses} - {self.ties}\n"
#     def addResult(self, result):
#         if result == 1:
#             self.wins += 1
#         elif result == 0:
#             self.ties += 1
#         elif result == -1:
#             self.losses += 1






# def get_random_rps():
#     rps = ["r", "p", "s"]
#     return rps[random.randrange(0,3)]


# def eval_rps(player_cmd, computer_cmd):
#     if player_cmd == "r":
#         if computer_cmd == "p":
#             return -1
#         elif computer_cmd == "s":
#             return 1
#         elif computer_cmd == "r":
#             return 0
#     elif player_cmd == "p":
#         if computer_cmd == "p":
#             return 0
#         elif computer_cmd == "s":
#             return -1
#         elif computer_cmd == "r":
#             return 1
#     elif player_cmd == "s":
#         if computer_cmd == "p":
#             return 1
#         elif computer_cmd == "s":
#             return 0
#         elif computer_cmd == "r":
#             return -1

# choice_dictionary = {"r": "rock", "p": "paper", "s": "scissors"}






# p = Player(input("What is your name? "))


# while True:
#     agent_choice = get_random_rps()
#     print(p)
#     cmd = input("-> ")
#     if cmd == "q":
#         break
#     elif cmd == "r" or cmd == "p" or cmd == "s":
#       result = eval_rps(cmd, agent_choice)
#       print(f"You chose {choice_dictionary[cmd]}")
#       print(f"Computer chose {choice_dictionary[agent_choice]}")
#       p.addResult(result)
#       if result == 1:
#           print("You win!")
#       elif result == 0:
#           print("Tie")
#       else:
#           print("You lose")
#     else:
#         print("I did not understand that command.")```