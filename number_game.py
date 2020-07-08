"""
Classrom work
"""

import random

is_playing = True

while is_playing:
    # give game start message to the user that explains the game and waht is expected
    print("Welcome to GUESS THE NUMBER! I hope you have fun!")

    # initialize a random number at the beginning of the game 
    number_to_guess = random.randint(1, 100)

    user_has_won = False
    # need a guessing loop that runs until user guesses correctly 
    while not user_has_won:
        # promt the user for their input
        user_guess = int(input("I'm thinking of a number between 1 and 100. Guess which number i'm thinking of: "))
        # TODO: provide data to the user about the game (number of guesses so far?)
        # TODO: do some error checking on the user input

        # if the user is right 
        if user_guess == number_to_guess:
            user_has_won = True
            # program alerts user they won and asks if they want to play again or exit
            print("You guessed right! Good job!")

            play_again = input("Would you like to play again? Y or N?")
            if play_again.lower() =="n":
                is_playing = False
        # if the user is wrong
        # programm alerts user that guess was wrong if it was too high or to low
        elif user_guess > number_to_guess:
            print("You guess was too high! Try again!")
        else:
            print("Your guess is too low! Try again!")
            
        
