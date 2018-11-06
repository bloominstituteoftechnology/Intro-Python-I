
import random

def guessing_game():
    print("\nGuess the number!")

    secret_number = random.randrange(101)

    while True:
        guess = input("\nInput your guess: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter an integer.")
            continue

        if guess == secret_number:
            print("You win!")
            break
        elif guess < secret_number:
            print("Too small!")
        else:
            print("Too big!")


if __name__ == '__main__':
    guessing_game()