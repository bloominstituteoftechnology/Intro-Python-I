"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python

#open file
file1 = open('foo.txt', 'r')

#read file
file_contents = file1.read()

# print file
print (file_contents)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# https://www.w3schools.com/python/python_file_write.asp

# make file
fil2 = open("bar.txt", "x")

fil2.write("This file \nis not \na pipe, nor a promise.||")
fil2.close()

#open file
file2 = open('bar.txt', 'r')

#read file
file_contents2 = file2.read()

# print file
print (file_contents2)