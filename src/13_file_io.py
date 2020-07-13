"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# old method - use context manager
# f = open('foo.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close() #must close 

# Use context manager
with open('foo.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open('bar.txt', 'r+') as f:
    f_contents = f.read()
    f.write('This is line 1\n')
    f.write('This is line 2\n')
    f.write('This is line 3\n')
    print(f_contents)
    f.closed
    




