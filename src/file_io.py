"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open('foo.txt')
data = f.read()
print(data)
f.close()

# with open('foo.txt') as f:
#   data = f.read()
#   print(data)
# f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as file:
  data = f"this is a line\nhere we have another line\npython rocks!"
  file.write(data)
f.closed

file = open('bar.txt')
print(file.read())
file.close()