"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# Close the file

# YOUR CODE HERE
f = open('foo.txt', 'r')
print(f.read())
# f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
b = open('bar.txt', 'w')
b.write('Let`s kill this love\n')
b.write('yeah yeah yeah yeah yeah\n')
b.write('Rum, pum, pum, pum, pum, pum, pum')
b.close()
bf = open('bar.txt','r')
print(bf.read())