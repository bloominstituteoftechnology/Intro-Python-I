"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
import os
filePath = (f'{os.getcwd()}\src\\foo.txt')
with open(filePath) as f:
    print(f.read())
f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

filePath = (f'{os.getcwd()}\src\\bar.txt')
with open(filePath, mode='w') as f:
    for i in range(3):
        print(
            f'Write three lines of arbitrary content to that file {i+1}', file=f)
f.closed
