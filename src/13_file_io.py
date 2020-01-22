"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:


"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

file = open('foo.txt', "r")
print(file.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

file = open('bar.txt', 'w')

file.write('Hello')
file.write('This is Cam')
file.write('What\s going on')

file.close()
