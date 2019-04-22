"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

foo = open('foo.txt', 'r')
print(foo.read())
foo.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar = open('bar.txt', 'w')
bar.write("this is amazing!  I can't believe this works!")
bar.close()
new_bar = open('bar.txt', 'r')
print(new_bar.read())
