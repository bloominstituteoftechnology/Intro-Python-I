# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = int(input("Enter a number: "))

def is_even(n):
  if n%2 == 0:
    print("Even!")
  else:
    print("Odd")

is_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"