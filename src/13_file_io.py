"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
object2 = open('foo.txt', 'r')
str = object2.read()
print(str)

object2.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

obj_bar = open('bar.txt', 'w')
obj_bar.write("Line 1\n Yeah its great!\n New line")
obj_bar.close()
objec_read = open('bar.txt', 'r')
str2 = objec_read.read()
print(str2)
objec_read.close()