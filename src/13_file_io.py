"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
#prints all the lines in the file
file = open('foo.txt', mode='rt')


for line in file:
    print(line)

file.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
file = open('bar.txt', 'w')
# writing. Write three lines of arbitrary content to that file,
file.write(

    """
    Line1
    Line2
    Line3
    """
)

file.close()
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
