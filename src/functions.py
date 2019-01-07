# Write a function is_even that will return true if the passed-in number is even.

def is_even(n):
  return False if n % 2 else True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def is_even_printer():
  if is_even(num) == True:
    print('Even!')
  else:
    print('Odd')
is_even_printer()
