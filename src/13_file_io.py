"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# importing the os to get the path to find the file
import os

fooPath = os.path.join(os.path.dirname(__file__),  "foo.txt")



# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# opening the file
f = open(fooPath)
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# making the path for the bar file
barPath = os.path.join(os.path.dirname(__file__), "bar.txt")

# opening the path
theFile = open(barPath, "w")
theFile.write("Hey this is the first line in the bar file.\n")
theFile.write("This is the second line of the file, yeah!\n")
theFile.write("This is now the third line of the file!\n")
theFile.close()
