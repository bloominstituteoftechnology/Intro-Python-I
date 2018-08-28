import random


class RPSAgent:
    def __init__(self, preferred_selection=1):
        self.preferred_selection = preferred_selection
    def getMove(self):
        """
        This will get a move with some bias built in.
        """
        randNumber = random.random()
        if self.preferred_selection == 1:
            if randNumber <= 0.6:
                return 1
            elif randNumber <= 0.8:
                return 2
            else:
                return 3
        elif self.preferred_selection == 2:
            if randNumber <= 0.6:
                return 2
            elif randNumber <= 0.8:
                return 3
            else:
                return 1
        else:
            if randNumber <= 0.6:
                return 3
            elif randNumber <= 0.8:
                return 1
            else:
                return 2





agent = RPSAgent(random.randint(1,3))

score = {"wins": 0, "losses": 0, "ties": 0}

while True:
    inp = input("\nWhat is your input (r/p/s): ")
    computer_selection = agent.getMove()
    if computer_selection == 1:
        print ("\nComputer picks Rock")
    elif computer_selection == 2:
        print ("\nComputer picks Paper")
    elif computer_selection == 3:
        print ("\nComputer picks Scissors")
    if inp == "q":
        break
    elif inp == "r":
        if computer_selection == 1:
            score["ties"] += 1
            print ("Tie")
        elif computer_selection == 2:
            score["losses"] += 1
            print ("Loss")
        elif computer_selection == 3:
            score["wins"] += 1
            print ("Win")
    elif inp == "p":
        if computer_selection == 1:
            score["wins"] += 1
            print ("Win")
        elif computer_selection == 2:
            score["ties"] += 1
            print ("Tie")
        elif computer_selection == 3:
            score["losses"] += 1
            print ("Loss")
    elif inp == "s":
        if computer_selection == 1:
            score["losses"] += 1
            print ("Loss")
        elif computer_selection == 2:
            score["wins"] += 1
            print ("Win")
        elif computer_selection == 3:
            score["ties"] += 1
            print ("Tie")
    elif inp == "score":
        print("Wins: %d, Losses: %d, Ties: %d" % (score["wins"], score["losses"], score["ties"]))
    elif inp == "agent":
        print(agent.preferred_selection)
    else:
        print ("I did not recognize that command")