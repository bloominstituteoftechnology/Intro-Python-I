"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt', 'rt') as F:
    print(F.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'wt') as F:
    F.writelines(["key: population  value: 121240\n",
    "key: founded  value: March 23, 1868\n",
    "key: monster  value: goblin\n"])

with open('bar.txt', 'rt') as F:
    print(F.read())
