"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

import os.path

path = os.path.dirname(__file__)
fooPath = os.path.join(path, 'foo.txt')

with open(fooPath) as f:
    for line in f:
        print(line, '\n')

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

text = '''Test First Line.
Test Second Line.
Test Third Line.'''

barPath = os.path.join(path, 'bar.txt')

with open(barPath, 'w') as f:
    f.write(text)

f.close()

with open(barPath) as f:
    for l in f:
        print(l, '\n')

f.close()