"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# The file should be relative to where you're executing the python command

# YOUR CODE HERE
with open('./foo.txt', 'r+') as f:
  for line in f:
    print(line)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('./bar.txt', 'w+') as f:
  f.writelines('Whatever is this\n')
  f.writelines('This is an arbitrary assignment\n')
  f.writelines('Blah blah blah\n')

with open('./bar.txt', 'r+') as f:
  for line in f:
    print(line)