# Write a function is_even that will return true if the passed in number is even.
def is_even(num):
  if num % 2 == 0:
    print('true')

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
def even_or_odd(num):
  if int(num) % 2 == 0:
    print('Even')
  else:
    print('Odd')

even_or_odd(num)