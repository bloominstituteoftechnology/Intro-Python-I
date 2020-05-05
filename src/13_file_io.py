"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

f = open('foo.txt', 'r')
f = f.read()
print(f)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

my_f = open('bar.txt', 'w+')

my_f.write("Quoting Shakespeare is a little dated, don't you think? \n")

my_f.write("Let's pick out some modern snark to laugh at. \n")

my_f.write("'She say that I glow below the waist and a stroke is just so PGA' - Small Worlds, Mac Miller \n")

my_f.close()

# YOUR CODE HERE