"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
file = open('foo.txt', 'r')

with open('foo.txt') as file:
  read_data = file.read()
  print(read_data)
  file.close()
True

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
newFile = open('bar.txt', 'w')

with open('bar.txt', 'w') as newFile:
  write_data = newFile.write("\nThis is new text\nthat I'm adding\nto the file")
  newFile.close()

with open('bar.txt') as newFile:
  read_data = newFile.read()
  print(read_data)
