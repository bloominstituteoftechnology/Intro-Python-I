# Write a function is_even that will return true if the passed-in number is even.

def is_even(number):
    print(number % 2 == 0)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def even_odd(number):
    if number == 0:
        print('Nice try...')
        number = input('Try again: ')
        number = int(number)
        even_odd(number)
    elif number % 2 == 0:
        is_even(number)
        print('Even!')
    else:
        is_even(number)
        print('Odd!')
even_odd(num)
