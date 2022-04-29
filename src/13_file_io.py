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

# get the file path relative to the current script
my_path = os.path.dirname(__file__)
foo_path = os.path.join(my_path, 'foo.txt')

with open(foo_path) as f:
    print('Contents of \'foo.txt\':')
    for line in f:
        print('    ' + line, end='')

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
arbitrary_text = '''First line of arbitrary text.
Second line of arbitrary text.
Third line of arbitrary text.'''

bar_path = os.path.join(my_path, 'bar.txt')

# Create (or overrite existing) file and write arbitrary text
with open(bar_path, 'w') as f:
    f.write(arbitrary_text)

f.close()

# Open newly created file and print its contents
with open(bar_path) as f:
    print('\nContents of \'bar.txt\':')
    for line in f:
        print('    ' + line, end='')

f.close()
