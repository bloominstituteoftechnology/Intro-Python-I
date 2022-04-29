"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt') as f:
    read_data = f.read()
    print(read_data)

# The with keyword closes the file automatically 
# - this returns true if the file is actually closed
f.closed 

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('bar.txt', 'w') as o:
    o.write("This is line 1 of arbitrary text. \nIt can be difficult to write arbitrary text because of its arbitrary nature. \nIt's important not to be too cavalier with arbitrary text as to not accidentally inflate its importance.")

with open('bar.txt') as p:
    p_data = p.read()
    print(p_data)
