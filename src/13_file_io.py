"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt') as f:
    read_data = f.read()
print(read_data)
# Check that the file has been automatically closed
print(f.closed)     # Should return True


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file.

f = open('bar.txt', 'w')
f.write('This is the first line.\nThis is the second line.\nThis is the third line.')
f.close()

# Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open('bar.txt') as f:
    read_data = f.read()
print(read_data)