"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
file = open("foo.txt", "r")
# ROMEO AND JULIET GOOD STUFF
print(file.read())
file.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

file = open("bar.txt", "w")
Lines = ["Is this the real life?\n", "Is this just fantasy?\n",
"Caught in a landslide\n", "No escape from reality\n"]


file = open("bar.txt", "w")
file.writelines(Lines)
file.close()

file = open("bar.txt", "r")
print(file.read())
file.close()
