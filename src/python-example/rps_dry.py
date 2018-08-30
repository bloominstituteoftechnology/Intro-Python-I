import random


class RPSAgent:
    def __init__(self, preference=0):
        self.nonpreferred = ["r", "p", "s"]
        self.preferred = self.nonpreferred.pop(preference)
    def getMove(self):
        """
        This will get a move with some bias built in.
        """
        randNumber = random.random()
        if randNumber <= 0.6:
            return self.preferred
        elif randNumber <= 0.8:
            return self.nonpreferred[0]
        else:
            return self.nonpreferred[1]



def evalRPS(playerMove, opponentMove, score):
    if playerMove == opponentMove:
        print("Tie")
        score["ties"] += 1
    elif playerMove == "r" and opponentMove == "p" \
           or playerMove == "p" and opponentMove == "s" \
           or playerMove == "s" and opponentMove == "r":
        print ("Loss")
        score["losses"] += 1
    elif playerMove == "r" and opponentMove == "s" \
           or playerMove == "p" and opponentMove == "r" \
           or playerMove == "s" and opponentMove == "p":
        print ("Win!")
        score["wins"] += 1
    return score


agent = RPSAgent(random.randint(0,2))
picksHumanized = {"r":"rock", "p": "paper", "s": "scissors"}

score = {"wins": 0, "losses": 0, "ties": 0}

while True:
    inp = input("\nWhat is your input (r/p/s): ")
    computer_selection = agent.getMove()
    if inp == "q":
        break
    elif inp == "r" or inp == "p" or inp == "s":
        print ("\nComputer picks %s." % picksHumanized[computer_selection])
        score = evalRPS(inp, computer_selection, score)
    elif inp == "score":
        print("Wins: %d, Losses: %d, Ties: %d" % (score["wins"], score["losses"], score["ties"]))
    elif inp == "agent":
        print(agent.preferred)
    else:
        print ("I did not recognize that command")