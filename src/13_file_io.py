"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

foo = 'C:\\Users\\dakot\\Documents\\GitHub\\Intro-Python-I\\src\\foo.txt'
with open(foo) as f:
    read = f.read()
    print(read)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
arbitrary = '''I believe I have seen a face!
Well did it have a nose?
Yes! It did have a nose!!
Yes yes, That does sound like a face.'''

bar = 'C:\\Users\\dakot\\Documents\\GitHub\\Intro-Python-I\\src\\bar.txt'
with open(bar, 'w') as k:
    write = k.write(arbitrary)


# test that it works!

with open(bar) as j:
    readit = j.read()
    print(readit)
