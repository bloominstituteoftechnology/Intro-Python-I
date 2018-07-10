# Write a function is_even that will return true if the passed in number is even.
def is_even(num):
  return (num % 2) == 0

# Read a number from the keyboard
myNum = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
myNum = int(num)
if is_even(myNum):
  print("Even!")
else:
  print("Odd!")