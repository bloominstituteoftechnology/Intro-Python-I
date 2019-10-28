"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

import os

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

dirname = os.path.dirname(os.path.abspath(__file__))

f = open(dirname + '\\foo.txt', 'r')

for line in f:
  print(line, end='')

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

new_file = open(dirname + '\\bar.txt', 'x')

new_file.write(
'This is line 1.\nThis is line 2.\nThis is line 3.' 
)

new_file.close()