# Write a function is_even that will return true if the passed in number is even.

def is_even(num) :
    if num % 2 == 0 :
        return True
    elif num % 2 != 0 :
        return False

print(is_even(19))

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(int(num)) :
    print('Even!')
else :
    print('Odd')
    