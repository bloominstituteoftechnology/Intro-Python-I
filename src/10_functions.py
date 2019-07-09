# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(a_num):
    if a_num % 2 == 0:
        return True
    else:
        return False

print(is_even(11))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# if num % 2 == 0:
#     print('EVEN!')
# else:
#     print('Odd')
def even_input(a_num):
    if a_num % 2 == 0:
        print('Even!')
    else:
        print('Odd')

even_input(num)

