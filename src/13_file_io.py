"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

import os


def find_in_subdirectory(filename, subdirectory=''):
    if subdirectory:
        path = subdirectory
    else:
        path = os.getcwd()
    for root, dirs, names in os.walk(path):
        if filename in names:
            return os.path.join(root, filename)
    raise 'File not found'

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note:
# Pay close attention to your current directory when trying to open "foo.txt"


# YOUR CODE HERE
with open(find_in_subdirectory('foo.txt'), 'r') as foo:
    for line in foo:
        print(line, end='')

print()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('./src/bar.txt', 'w') as bar:
    bar.write("Happy times ahead.\n")
    bar.write("Lambda CS is awesome!\n")
    bar.write("This is not a drill.\n")
