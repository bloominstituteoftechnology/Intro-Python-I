"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('src/foo.txt') as f:
    read_data = f.read()
    print(read_data)
    f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('src/bar.txt', 'a') as g:
    g.write("I am slowly going crazy \n Crazy going slowly am I \n Become a computer programer, they said\n It would be fun, they said")
    g.close()
    
with open('src/bar.txt') as h:
    read_data = h.read()
    print(read_data)
    h.close()