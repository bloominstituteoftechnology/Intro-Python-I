"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# Using with, it is closed automatically
# YOUR CODE HERE

with open("Intro-Python-I/src/foo.txt") as file_obj:
    for line in file_obj:
        print(line)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# 
with open("Intro-Python-I/src/bar.txt", "w") as file_obj:
    file_obj.write("yo \n yo \n yo")