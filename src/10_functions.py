# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def isEven(num):
  if type(num) == int:
    return num%2==0;
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def declareEven(num):
  return (isEven(num) and "Even!" ) or "Odd"
print(isEven(5))
print(isEven(10))
print(isEven("a"))
print(declareEven(num))
print(declareEven(5))
print(declareEven(4))