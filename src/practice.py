
import random


def guessing_game():
    ptint("Guess the number")
    secret_number = random.randrange(101)
# print(secret_number)


while True:
    guess = input("input your guess:")

try:
            guess = int(guess)
            except ValueError:
                print("please enter an integer.")
                continue

                print(f"You guessed:{guess}")
                if guess == secret_number:

    print("you win!")
    break
    elif guess secret_number:
    print("too small")
    else:
        print("Too big")
        return play_again

    # if __name__ == '__main__':
guessing_name()
