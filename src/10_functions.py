# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
  return(x%2==0)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def call(num):
  even=is_even(num)
  if even:
    print('Even')
  else:
    print('Odd')
# YOUR CODE HERE

call(num)