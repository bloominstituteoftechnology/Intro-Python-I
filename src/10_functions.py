# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def even_function(l):
    for i in range(len(l)):
        l[i] % 2 == 0
        return l
    
z = [2, 4, 6, 7]    
print(z)
even_function(z)

print(z)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def shout_function(l):
    for i in range(len(l)):
        l[i] % 2 == 0
        print("Even!")
    else:
      print("Odd!")
