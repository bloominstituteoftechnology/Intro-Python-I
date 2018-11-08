import random

guessesTaken = 0
print("Hello, what is your name?")
myName = input()

number = random.randint(1, 20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

while guessesTaken < 6:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

        if guess == number:
            break

if guess == number:
    guessesTaken = str(guessesTaken)
    print(f'\'Good job, {myName} you can start your treasure hunt!\'')
if guess != number:
    number = str(number)
    print(f"Nope.The number I was thinking of was\",{number}")
