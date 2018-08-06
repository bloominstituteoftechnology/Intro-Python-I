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
alphabet = [chr(65+x) for x in range(0, 26) ]

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
    if not user_letter.isalpha():
        print("Invalid input, please input lower-case letters a-z")
        continue
    if user_letter.isalpha():
        if len(user_letter) > 1:
            print("Pick one letter at a time!")
            continue
        else:
            user_letter = user_letter.lower()
            for i in range(len(target_word)):
                if user_letter in cur_word:
                    print("You already picked that letter! ")
                    continue
                elif user_letter == target_word[i]:
                    cur_word[i] = user_letter 
                    if ''.join(cur_word) == ''.join(target_word):
                        print("Congratulations! You win!")
                        print("**************************")
                        print(''.join(cur_word).upper())
                        print("**************************")
                        break
                else:
                    strikes += 1
                    if strikes == len(target_word):
                        print("Too bad, you lose!")
                        break
                    


    