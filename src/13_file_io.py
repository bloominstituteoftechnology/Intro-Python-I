"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

f = open('foo.txt', 'r')
print(f.read())
f.close()
print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

f = open('bar.txt', 'w')
f.write("The fox ran over the hill")
f.close()
print(f.closed)
f = open('bar.txt', 'r')
print(f.read())
f.close()
print(f.closed)
# YOUR CODE HERE