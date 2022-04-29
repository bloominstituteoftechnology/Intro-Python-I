"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os

parent_path = os.path.dirname(__file__)
foo_path = os.path.join(parent_path, 'foo.txt')

read_only = open(foo_path, 'r')
for line in read_only:
    print(end='-')
    print('  ' + line, end='')

read_only.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar_path = os.path.join(parent_path, 'bar.txt')

arbitrary_text = '''First line of arbitrary text.
Second line of arbitrary text.
Third line of arbitrary text.'''

write_only = open(bar_path, 'w')
write_only.write(arbitrary_text)
write_only.close()

# read bar.txt

read_bar = open(bar_path, 'r')
for line in read_bar:
    print(end='-')
    print('  ' + line, end='')

read_bar.close()



