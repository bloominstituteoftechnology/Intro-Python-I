# Write a function is_even that will return true if the passed in number is even.
def is_even(x):
  return x % 2 == 0

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
num = int(num)

if is_even(num):
  print("Even!")
else:
  print("Odd!")

"""
Alternative:
def oddEven(n):
  if int(n) % 2 == 0:
    print("Even!")
  else:
    print("Odd")

oddEven(num)
"""