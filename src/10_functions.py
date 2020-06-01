# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def even_odd(x):
    if x % 2 == 0:
<<<<<<< HEAD
        print('Even')
    else:
        print('Odd')

even_odd(num)
=======
        answer = 'Even!'
    else:
        answer = 'Odd!'
    return answer

print(even_odd(num))
>>>>>>> 445160f5a5274fb7fb007873da70e0c8dbed8d2b
