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

my_path = os.path.dirname(__file__)
foo_path = os.path.join(my_path, 'foo.txt')

with open(foo_path) as f:
    for line in f:
        print(line, '\n')

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

my_text = '''This is some text for the first line.
This is some text for a second line.
This is some text for a third line.'''

bar_path = os.path.join(my_path, 'bar.txt')

with open(bar_path, 'w') as f:
    f.write(my_text)

f.close()

with open(bar_path) as f:
    for line in f:
        print(line, '\n')

f.close()