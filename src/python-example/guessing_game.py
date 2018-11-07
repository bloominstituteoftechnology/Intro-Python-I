import random

def guessing_game():
    print("Guess the number!")

    secret_number = random.randrange(101)
    #print(secret_number)

    while True:
        guess = input("input your guess: ")

        try:
            guess  = int(guess)
        except ValueError:
            print("Please enter an integer")
            continue
        if guess == secret_number:
            print("You win!")
            #play_again = play_again(input("Play again?"))
            break
        elif guess < secret_number:
            print("too small")
        else:
            print("too big")

if __name__ == '__main__':
    guessing_game()

