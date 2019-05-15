"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

f = open("foo.txt", "r")
print(f.read())
# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain
g = open("bar.txt", "w")
g.write("Hello\n")
g.write("Goodbye\n")
g.write("Why do you say Goodbye?\n")
g.close()
g = open("bar.txt", "r")

print(g.read())

# YOUR CODE HERE