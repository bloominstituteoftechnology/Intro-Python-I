#What is a  game loop?
import random

def guessing_game():
    print("Guess the Number!")

    secret_number = random.randrange(101)
    #computer picks a ranomd numer should be between 1 and 100 ^

    #this is the loop, until the number is guessed it keeps going
    while True:
        guess = input(" Input your guess: ")
        
        #try accept block to make sure what is inputed is an integer aka whole number
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter only integers.")
            continue
        
        print(f"You guessed: {guess}")


        if guess == secret_number:
            print("You win!")
            break
        elif guess < secret_number:
            print("too small!")
        else:
            print("too big!")

if __name__ == '__main__':
    guessing_game()

#to play the game go to terminal type python guessing_game.py