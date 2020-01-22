"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
files = open('C:\\user\\Desktop\\Lambda School Projects\\Intro-Python-I\\src\\foo.txt')
print(files.read())
files.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
fileTwo = open('C:\\user\\Desktop\\Lambda School Projects\\Intro-Python-I\\src\\bar.txt', 'w+')
fileTwo.write('Python is awesome.\nI will always love JavaScript my first love\\Both languages will work hand in hand for building scalable software')
fileTwo.close()
fileTwo = open('C:\\user\\Desktop\\Lambda School Projects\\Intro-Python-I\\src\\bar.txt')
print(fileTwo.read())
fileTwo.close()