# Write a function is_even that will return true if the passed in number is even.

def is_even(x):
  return x%2==0

# Read a number from the keyboard
num = input("Enter a number: ")


someBool = is_even(num)
if(someBool):
  print("Even!")
else:
  print("Odd")

# Print out "Even!" if the number is even. Otherwise print "Odd"