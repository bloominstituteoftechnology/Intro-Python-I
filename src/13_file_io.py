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

script_dir = os.path.dirname(__file__)
rel_path = 'foo.txt'
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as f:
    read_data = f.read()

f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open("bar.txt", "a") as f:
    f.write("This is it")

f.closed

script_dir = os.path.dirname(__file__)
rel_path = 'bar.txt'
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    read_data = f.read()

f.closed