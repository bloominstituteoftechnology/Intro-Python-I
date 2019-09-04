# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num): 
  if (num % 2 == 0):
    return f'Even!'
  return f'Odd!'

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"
