# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


# YOUR CODE HERE
def is_even(num):
  if (num % 2) == 0:
      print("{0} is an even number!".format((num)))
  else:
      print("{0} is an odd number!".format((num)))
is_even(num)
