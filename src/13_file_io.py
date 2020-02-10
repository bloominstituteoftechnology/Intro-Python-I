"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open('/Users/jakeconnerly/Desktop/iOS9/introToPythonI/Intro-Python-I/src/foo.txt', 'r')
x = f.read()
print(x)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

b = open('bar.txt', 'w+')
b.write("This is the first line.\n This is the second. \n Who'd a guessed this was third.")
b.flush()
b.seek(0)
print(b.read())
b.close()