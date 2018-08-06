import random

bodies = [ " ------\n |    |\n |    O\n |\n |\n |\n |\n |\n---", 
" ------\n |    |\n |    O\n |    |\n |    |\n |\n |\n |\n---", 
" ------\n |    |\n |    O\n |    |\n |    |\n |   / \n |\n |\n---", 
" ------\n |    |\n |    O\n |    |\n |    |\n |   / \ \n |\n |\n---", 
" ------\n |    |\n |    O\n |   \|\n |    |\n |   / \ \n |\n |\n---",
" ------\n |    |\n |    O\n |   \|/\n |    |\n |   / \ \n |\n |\n---" ]
strikes = 0
words = [None]
file = open("words.txt", "r")
for line in file:
    words.append(line)
file.close()
# target_word = words[random.randint(0, len(words))]
target_word = list('word')
length = len(target_word)
cur_word = list("*" * length)
used = []

# Draw body based on # of incorrect guesses
def drawBody():
    print(bodies[strikes])

def print_word(word):
    print('-'.join(word))

while True:
    print('**********HANGMAN***********')
    print('\n')

    drawBody()
    
    print('\n')
    print_word(cur_word)
    print('-------------------------------------')
    user_letter = input("Please pick a letter: ")
    print('\n')
    if user_letter in used:
        print("You picked that one already!")
        continue
    if user_letter.isalpha():
        user_letter = user_letter.lower()
        if len(user_letter) > 1:
            print("One letter at a time!!")
            continue
        else:
            used.append(user_letter)
            if user_letter in target_word:
                for i in range(len(target_word)):
                    if target_word[i] == user_letter:
                        cur_word[i] = user_letter
            else:
                print('Letter not in word, try again!!')
                strikes += 1
            if strikes >= 5:
                drawBody()
                print("Out of guesses, you lose!")
                break
            if ''.join(target_word) == ''.join(cur_word):
                print('------------------------------')
                print('CONGRATULATIONS, YOU WIN!!!')
                print('------------------------------')
                print(''.join(cur_word).upper())
                print('------------------------------')
                break
                    
    else:
        print("Pick a letter between a-z!!")

    