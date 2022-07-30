# python3 src/13_file_io.py

"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open("src/foo.txt", "r")
file_contents = f.read()
print('\n')
print(file_contents)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open("src/bar.txt", "w")
f.write("I once knew a man who lived in a jar.\nFor a stranger sight you'd have to go far.\nI asked him once why he lived in a jar.\nHe grimaced and said, how bizarre you are." )
f.close()

f = open("src/bar.txt", "r")
file_contents = f.read()
print('\n')
print(file_contents)
print('\n')
f.close()
