"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "foo.txt")
with open(lines) as f:
    d = f.read()
    print(d)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
dir_path = os.path.dirname(os.path.realpath(__file__))
boo = os.path.join(dir_path, "foo.txt")

bar = open(boo, 'w')
bar.write('This\n')
bar.write('This is\n')
bar.write('This is test')
bar.close()

with open(boo) as bar:
    data = bar.read()
    print(data)
