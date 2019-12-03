"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

foo = open('/Users/nathanvanwyck/Lambda/CS/Intro-Python-I/src/foo.txt', 'r')
print(foo.read())
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open('/Users/nathanvanwyck/Lambda/CS/Intro-Python-I/src/bar.txt', 'w')
bar.write((
    'This is a line of arbitrary content.\n'
    'This, too, is a line of arbitrary content.\n'
    'In conclusion, this is a line of arbitrary content.'))
bar.close()
bar = open('/Users/nathanvanwyck/Lambda/CS/Intro-Python-I/src/bar.txt', 'r')
print(bar.read())
bar.close()
