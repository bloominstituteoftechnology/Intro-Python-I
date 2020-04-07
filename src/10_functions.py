# write a function is_even that will return true if the passed-in number is even

def is_even(number):
    if number % 2 == 0:
        print('even!')
    else:
        print('odd')

# read a number from the keyboard

num = input('enter a number: ')
num = int(num)

# print out 'even!' if the number is even, otherwise print 'odd'

is_even(num)