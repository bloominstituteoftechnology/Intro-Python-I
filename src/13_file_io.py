"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# Use a context manager to open the file, so it doesn't have to be explicitly closed
with open("foo.txt", "r") as fr:
    print(fr.read())


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

three_arbitrary_lines = """Me? I'm dishonest, and a dishonest man you can always trust to be dishonest.
Honestly.
It's the honest ones you want to watch out for, because you can never predict when they're going to do something incredibly...stupid."""

# Write the above lines to a new file
with open("bar.txt", "w") as fw:
    fw.write(three_arbitrary_lines)

# Confirm the written contents
with open("bar.txt", "r") as file:
    print(file.read())

