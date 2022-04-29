"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open("foo.txt", "r")
with open('foo.txt') as f:
    files = f.read()
    print(files)
    f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
d = open("bar.txt", "w")
with open('bar.txt') as f:
    d.write("We are the champions.\n")
    d.write("This is the second line.\n")
    d.write("This is the end.\n")
    d.close()
c = open("bar.txt", "r")
with open('bar.txt') as c:
    print(c.read())
