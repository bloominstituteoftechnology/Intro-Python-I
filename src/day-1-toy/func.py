# Write a function is_even that will return true if the passed in number is even.
def is_even(num):
    if num % 2 == 0:
        print('Even!')
    else:
        print('Odd!')
# Read a number from the keyboard
num = int(input("Enter a number: "))

# Print out "Even!" if the number is even. Otherwise print "Odd"
is_even(num)
