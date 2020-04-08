"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
# Read or Read and Write properties

# Open up the "foo.txt" file (which already exists) for reading
file = open("foo.txt", "r")

# Print all the contents of the file, then close the file
print(file.read())
file.close()
# Note: pay close attention to your current directory when trying to open "foo.txt"
# NOTE: definitely need to change directory to open...ls > cd src/ > then hit run


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

file_bar = open("bar.txt", "w")
lines = ["Quarantine!\n", "Quarantine!\n", "Quarantine!\n"]
file_bar.writelines(lines)
file_bar.close()

# Verify it worked
file2 = open("bar.txt", "r")
print(file2.read())
