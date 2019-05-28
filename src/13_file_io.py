"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

myFile = open('foo.txt', 'r')
print(myFile.read())
myFile.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

myFile2 = open('bar.txt', 'w')
myFile2.write('Learning how to write scripts')
myFile2.close()
new_file = open('bar.txt', 'r')
print(new_file.read())