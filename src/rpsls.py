import random


dict = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}

win = " You win!"
loss = " You lose."
rock_paper = "Paper covers rock."
rock_scissors = "Rock crushes scissors."
rock_lizard = "Rock crushes lizard."
rock_spock = "Spock vaporizes rock."
paper_scissors = "Scissors cuts paper."
paper_lizard = "Lizard eats paper."
paper_spock = "Paper disproves Spock."
scissors_lizard = "Scissors decapitates lizard."
scissors_spock = "Spock smashes scissors."
lizard_spock = "Lizard poisons Spock."

def game():
    u = int(input("1-Rock, 2-Paper, 3-Scissor, 4-Lizard, 5-Spock. Shoot! "))
    x = random.randint(1,5)
    if type(u) == int:
        print("You: ", dict[u])
        print("Computer: ", dict[x])
        if u == x:
            print("Tie!")
        elif u == 1 and x == 2:
            print(rock_paper, loss)
        elif u == 1 and x == 3:
            print(rock_scissors, win)
        elif u == 1 and x == 4:
            print(rock_lizard, win)
        elif u == 1 and x == 5:
            print(rock_spock, loss)
        elif u == 2 and x == 1:
            print(rock_paper, win)
        elif u == 2 and x == 3:
            print(paper_scissors, loss)
        elif u == 2 and x == 4:
            print(paper_lizard, loss)
        elif u == 2 and x == 5:
            print(paper_spock, win)
        elif u == 3 and x == 1:
            print(rock_scissors, loss)
        elif u == 3 and x == 2:
            print(paper_scissors, win)
        elif u == 3 and x == 4:
            print(scissors_lizard, win)
        elif u == 3 and x == 5:
            print(scissors_spock, loss)
        elif u == 4 and x == 1:
            print(rock_lizard, loss)
        elif u == 4 and x == 2:
            print(paper_lizard, win)
        elif u == 4 and x == 3:
            print(scissors_lizard, loss)
        elif u == 4 and x == 5:
            print(lizard_spock, win)
        elif u == 5 and x == 1:
            print(rock_spock, win)
        elif u == 5 and x == 2:
            print(paper_spock, loss)
        elif u == 5 and x == 3:
            print(scissors_spock, win)
        elif u == 5 and x == 4:
            print(lizard_spock, loss)
    else:
        print("Please type a number between 1 & 5")
    play = (input("Play again? Y/N: "))
    if play == "Y" or play == "y":
        game()
    else:
        quit()


game()
