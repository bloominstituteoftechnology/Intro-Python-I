"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

file1 = open("./src/foo.txt", "r")
content = file1.read()
print(content)
file1.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

file2 = open("./src/bar.txt","w")
file2.write("Test 1\n")
file2.write("Test 2\n")
file2.write("Test 3\n")
file2.close() 

file2 = open("./src/bar.txt","r")
content = file2.read()
print(content)
file2.close()