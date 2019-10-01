"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os
os.chdir('./src')

with open('foo.txt', 'r') as f:
    for line in f:
        print(line)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as f:
    f.write('Beautiful is better than ugly.\n')
    f.write('Explicit is better than implicit.\n')
    f.write('Simple is better than complex.\n')
f.close()

with open('bar.txt', 'r') as f:
    for line in f:
        print(line)
f.close()