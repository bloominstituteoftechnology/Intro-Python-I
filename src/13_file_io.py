"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

def load_foo():
    text_file = open('foo.txt', 'r')
    text_data = text_file.read()
    text_file.close()
    return text_data
print(load_foo())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

def bar_file():
    text_file = open('bar.txt', 'w')
    text_file.write('line 1 \nline 2 \nline 3')
    text_file.close()

bar_file()
