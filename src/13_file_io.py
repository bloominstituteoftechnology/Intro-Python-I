"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os
f = open(os.path.join('src', 'foo.txt'), 'r')
print(f.read())
f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

f = open(os.path.join('src', 'bar.txt'), 'w')
f.write('Hello there\n')
f.write('THe angel from my nightmare\n')
f.write('The shadow in the background of the morgue\n')
f.close()