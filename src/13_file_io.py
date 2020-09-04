"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

my_file = open("foo.txt", "r")  # Open the file
print(my_file.read()) # Read the file 
my_file.close() # Close the file

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

new_file = open("bar.txt", "w")
new_file.write("""Python is an interpreted, high-level and general-purpose programming language. 
               It was created by Guido van Rossum and first released in 1991.
               Python's design philosophy emphasizes code readability with its notable use of significant whitespace.""")
new_file.close()