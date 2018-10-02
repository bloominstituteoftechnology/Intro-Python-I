import random


class Player():
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
    def __str__(self):
        return f"\n{self.name}\n{self.wins} - {self.losses} - {self.ties}\n"
    def addResult(self, result):
        if result == 1:
            self.wins += 1
        elif result == 0:
            self.ties += 1
        elif result == -1:
            self.losses += 1






def get_random_rps():
    rps = ["r", "p", "s"]
    return rps[random.randrange(0,3)]


def eval_rps(player_cmd, computer_cmd):
    if player_cmd == "r":
        if computer_cmd == "p":
            return -1
        elif computer_cmd == "s":
            return 1
        elif computer_cmd == "r":
            return 0
    elif player_cmd == "p":
        if computer_cmd == "p":
            return 0
        elif computer_cmd == "s":
            return -1
        elif computer_cmd == "r":
            return 1
    elif player_cmd == "s":
        if computer_cmd == "p":
            return 1
        elif computer_cmd == "s":
            return 0
        elif computer_cmd == "r":
            return -1

choice_dictionary = {"r": "rock", "p": "paper", "s": "scissors"}






p = Player(input("What is your name? "))


while True:
    agent_choice = get_random_rps()
    print(p)
    cmd = input("-> ")
    if cmd == "q":
        break
    elif cmd == "r" or cmd == "p" or cmd == "s":
      result = eval_rps(cmd, agent_choice)
      print(f"You chose {choice_dictionary[cmd]}")
      print(f"Computer chose {choice_dictionary[agent_choice]}")
      p.addResult(result)
      if result == 1:
          print("You win!")
      elif result == 0:
          print("Tie")
      else:
          print("You lose")
    else:
        print("I did not understand that command.")
