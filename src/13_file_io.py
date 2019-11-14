"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open('src/foo.txt', 'r')
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
g = open('src/bar.txt', 'w')
g.write("Whoop!! I'm writing a new line")
g.write("Whoops! I'm writing a second line")
g.write("Whoops! I'm writing a third line")
g.close()
t = open('src/bar.txt', 'r')
print(t.read())
t.close()