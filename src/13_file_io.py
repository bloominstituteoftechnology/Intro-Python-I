"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('src/foo.txt', 'r') as f:
    read_file = f.read()
    print(read_file)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('src/bar.txt', 'w') as b:
    content = b.write('''
    I am adding a couple of lines of text to this file
    I am really enjoying the intense coding of CS
    This is really cool''')
    b.close()

with open('src/bar.txt', 'r') as b:
    read_file = b.read()
    print(read_file)