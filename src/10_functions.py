# Write a function is_even that will return true if the passed-in number is even.
def is_even(number):
    if number % 2 == 0:
        return True

# Read a number from the keyboard

num = input("Enter a number: ")
num = int(num)

if num % 2 == 0:
    print('Even!')
else:
    print('Odd')    



