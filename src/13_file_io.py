"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os
PATH = os.getcwd()

filename = 'foo.txt'
def print_file(file= filename):
    with open(filename, mode='r') as f:
        for line in f.readlines():
            print(line)
print_file(filename)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
filename = 'bar.txt'
import this;

def write_lines(filename, num_lines):
    """ write to a new file n lines of garbage
    """
    with open(filename, mode='w') as newf:
        lines = []
        for _ in range(num_lines):
            lines.append(f"sometext\n")
        newf.writelines(lines)
        
write_lines(filename, 3)
print_file(filename)