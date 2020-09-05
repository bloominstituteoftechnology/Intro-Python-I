"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('src/foo.txt') as foo_file:
    read_data = foo_file.read()
    print(read_data)
    foo_file.close()

# YOUR CODE HERE

with open('src/bar.txt', 'w') as bar_file:
    bar_file.write("Hello World! \n")
    bar_file.write("Python is Great \n")
    bar_file.write("Cheesecake is also Great")
    bar_file.close()

""" opening bar file to checkif write was successful"""
with open('src/bar.txt') as bar_file:
    read_data = bar_file.read()
    print(read_data)
    bar_file.close()
    


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE