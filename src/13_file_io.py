"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open('/Users/Dahna/lambda-cs/Intro-Python-I/src/foo.txt', 'r')

print(f.read())
f.close()
# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar_file = open('bar.txt', 'w')
bar_file.write("I see now the circumstances of one's birth are irrelevant.\n It is what you do with the gift of life that determiens who you are. \n - Mewtwo")
bar_file.close()