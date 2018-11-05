import random

def guessing_game():
  print("Guess the number!")

  secret_number = random.randrange(101)

  while True:
    guess = input("Input your guess: ")
    
    try:
      value = int(guess)
    except ValueError:
      print("Please enter an integer.")

    print(f"You guessed: {value}")

    if value == secret_number:
      print("You win!")
      break
    elif value < secret_number:
      print("Too small!")
    else:
      print("Too big!")

if __name__ == '__main__':
  guessing_game()