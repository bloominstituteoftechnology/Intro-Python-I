"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
path = os.getcwd()
f = open(f"{path}/src/foo.txt", "r")
for line in f:
    print(line, end="")
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open(f"{path}/src/bar.txt", "w") as b:
    b.write("what\n")
    b.write("what no\n")
    b.write("what yes\n")
b.close()
