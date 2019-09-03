"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open("foo.txt") as f:
    for line in f:
        print(line, end="")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.text', 'w') as f:
    f.write('Lines are cool 1.\n')
    f.write('Lines are cool 2.\n')
    f.write('Lines are cool 3.\n')
    f.close()

with open('bar.text') as f :
    for line in f: 
        print(line, end='')