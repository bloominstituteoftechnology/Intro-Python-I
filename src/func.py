# Write a function is_even that will return true if the passed in number is even.

def even_number(num):
    if int(num) % 2 == 0:
        return True
    else:
        return False
# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
if even_number(num):
    print('You win!')
else:
    print('Odd one out again...')