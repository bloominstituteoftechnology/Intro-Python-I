"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:                                                                                 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('src/foo.txt', "r") as f:
    read_data = f.read()
    print(read_data)

print(f.closed) # good practice to use above "With" method instead of below when dealing with file obects; allows file to be properly closed even with exceptions.

# f = open("src/foo.txt", "r")
# data = f.read()
# print(data)
# f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('src/bar.txt', 'r+') as f:
    s = "Nothing to see here\nLiterally nothing.\nTry again grasshopper."
    f.write(s)
    f.close()
    print('finished writing', f.closed)


with open('src/bar.txt') as f:
    read_file = f.read()
    print(read_file)
    f.close()
    print(f.closed)