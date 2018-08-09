# There are at least 10 "mistakes" in this Hangman game
# These could include syntax errors, logical errors, spelling errors...
# Find the mistakes and fix the game!
#
# STRETCH GOAL: If you fix all the errors, can you find a way to improve
# it? Add a cheat code, more error handling, chose randomly
# from a set of win/loss messages...basically, make it better!

import random

# Initial setup
bodies = [ " ------\n |    |\n |    O\n |\n |\n |\n |\n |\n---",
" ------\n |    |\n |    O\n |    |\n |    |\n |\n |\n |\n---",
" ------\n |    |\n |    O\n |    |\n |    |\n |   / \n |\n |\n---",
" ------\n |    |\n |    O\n |    |\n |    |\n |   / \ \n |\n |\n---",
" ------\n |    |\n |    O\n |   \|\n |    |\n |   / \ \n |\n |\n---",
" ------\n |    |\n |  O\n |   \|/\n |    |\n |   / \ \n |\n |\n---" ]
strikes = 0
words = [None]
file = open("words.txt", "r")
for line in file:
    words.append(line)
file.close()
targetWord = words[random.randint(0, len(words))]
lettersLeft = len(targetWord)-1
length = len(targetWord)-1
print(length)
curWord = "_" * length
print(curWord)
alphabet = [chr(65+x) for x in range(26) ]

# Draw body based on # of incorrect guesses
def drawBody():
    print(bodies[strikes])

# Replace blanks with correctly guessed letters
def fillLetters( letter ):
    global curWord
    for i in range(len(targetWord)-1):
        if( targetWord[i]) == letter:
            curWord = curWord[0: i] + letter + curWord[i + 1: ]
            global lettersLeft
            lettersLeft -= 1

# Add spaces when displaying letters / blanks for readability
def printWord( word ):
    prntWord = ""
    for letter in word:
        prntWord += letter + " "
    print(prntWord)

# Begin game
print( "Welcome to Hangmn!" )
printWord(curWord)
drawBody()
print("Letters left:")
printWord(alphabet)

# Gameplay loop
while strikes < 5 and lettersLeft > 0:
    letter = input("\nPlease guess a letter...")
    if letter in targetWord:
        print("Great!")
        fillLetters(letter)
    else:
        strikes += 1
        print( str(strikes) + " / 5 strikes" )
    printWord(curWord)
    drawBody()
    try:
        alphabet.remove(letter.upper())
    except ValueError as e:
        pass
    print("Letters left:")
    printWord(alphabet)

# Game over, print outcome
if lettersLeft == 0:
    print("YOU WIN!!")
else:
    print("YOU LOSE...word was " + targetWord)