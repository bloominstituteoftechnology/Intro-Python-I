"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
foo = open("src/foo.txt", "r")
print(foo.read())
print(foo.close())


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', "w+") as f:
    f.write("This is a line.\n")
    f.write("This is another line.\n")
    f.write("This is a third line.")

with open('bar.txt') as f:
    read_data = f.read()
    print(read_data)