# Text-based space adventure game

import random
import time

def displayIntro():
    print("It is the end of a long year of fighting space criminals")
    print("you come to a crossroads on your trip home, one path leads home")
    print("where you will be handsomly rewarded for a job well done...")
    print("and the other leads through a gamma ray burst that will disentigrate you")
    print()

def choosePath():
    path = ""
    while(path != "1" and path != "2"): #input validation
        path = input('Which path will you choose? (1 or 2): ')

    return path

def checkPath(chosenPath):
    print('You head down the path...')
    time.sleep(2)
    print('Theres an asteroid nearby that looks familiar, that must be a good sign...')
    time.sleep(2)
    print('But your skin begins to tingle...')
    print()

    correctPath = random.randint(1,2)
    if(chosenPath == str(correctPath)):
        print("That tingling was just the feeling of admiration from the citizens of the galaxy!")
        print("Welcome home!")
    else:
        print("An extremely energetic burst of gamma rays pass through you")
        print("causing all of the atoms in your body to dissociate")
        print("There is no more record of your existence in this universe")
        print("You lost the game")

playAgain = "yes"
while playAgain  == "yes" or playAgain == "y":
    displayIntro()
    chosenPath = choosePath()
    checkPath(chosenPath)
    playAgain = input("Do you want to play again? (y or yes to continue playing)  ")
