# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
  if int(num) % 2 == 0:
    return True
  else:
    return False

num=4
print(is_even(num))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def oddEven(num):
  if int(num) % 2 == 0:
    print("Even!")
  else:
    print("Odd!")

oddEven(num)