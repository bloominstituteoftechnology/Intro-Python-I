"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open
# "foo.txt"

# YOUR CODE HERE
print("-----" * 2 + "BEGIN" + "-----" * 2)
f = open('src/foo.txt')
print("Opening file ...".upper())
print("Reading file:\n".upper(), f.read())
print("Closing file ...".upper())
f.close()
print("-----" * 5)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

b = open('src/bar.txt', 'w')
b.write(
    """This is a line of text. \n
    This is a new line.\n
    This is the last line."""
)
b.close()

print("Opening file ...".upper())
b = open("src/bar.txt")
print("Reading file:\n".upper(), b.read())
print("Closing file ...".upper())
b.close()
print("-----" * 2 + "DONE" + "-----" * 2)
